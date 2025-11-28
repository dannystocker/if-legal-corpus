"""ChromaDB ingestion for the legal corpus."""
from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path
from typing import List

import chromadb
from bs4 import BeautifulSoup
from chromadb.config import Settings
from pypdf import PdfReader


def read_manifest(manifest_path: str) -> List[dict]:
    with open(manifest_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def extract_text(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        reader = PdfReader(str(path))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    if path.suffix.lower() == ".json":
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return json.dumps(data)
    if path.suffix.lower() in {".html", ".xml", ".htm"}:
        with path.open("r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
        return soup.get_text("\n")
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def chunk_text(text: str, chunk_size: int = 1500, overlap: int = 200) -> List[str]:
    chunks: List[str] = []
    start = 0
    while start < len(text):
        end = min(len(text), start + chunk_size)
        chunks.append(text[start:end])
        start += max(1, chunk_size - overlap)
    return chunks


def ingest(manifest_path: str, db_dir: str) -> None:
    records = read_manifest(manifest_path)
    os.makedirs(db_dir, exist_ok=True)
    client = chromadb.PersistentClient(
        path=db_dir,
        settings=Settings(anonymized_telemetry=False),
    )
    collection = client.get_or_create_collection("if_legal_corpus")
    for record in records:
        if record.get("status") != "success":
            continue
        local_path = record.get("local_path")
        if not local_path or not os.path.exists(local_path):
            continue
        text = extract_text(Path(local_path))
        for idx, chunk in enumerate(chunk_text(text)):
            doc_id = f"{record.get('document_name')}-{record.get('sha256')}-{idx}"
            metadata = {
                "inventory_path": record.get("inventory_path"),
                "document_name": record.get("document_name"),
                "local_path": local_path,
                "sha256": record.get("sha256"),
            }
            collection.upsert(ids=[doc_id], documents=[chunk], metadatas=[metadata])
    client.persist()


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest downloaded corpus into ChromaDB")
    parser.add_argument(
        "--manifest",
        default="manifests/download_manifest.csv",
        help="Path to manifest CSV",
    )
    parser.add_argument(
        "--db-dir",
        default="indexes/chromadb",
        help="ChromaDB directory",
    )
    args = parser.parse_args()
    ingest(args.manifest, args.db_dir)


if __name__ == "__main__":
    main()
