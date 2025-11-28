# if-legal-corpus

Self-hosted legal document corpus for contract analysis and freelancer rights research. Contains international legislation, case law, and industry standards indexed in ChromaDB for semantic search.

## Quick Start

### Setup

```bash
# Clone repository (already done)
cd /home/setup/if-legal-corpus

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running Downloads

To download and process documents from the inventory:

```bash
# Download all documents from LEGAL_CORPUS_IMPORT_LIST.md
python scripts/download_all.py

# This will:
# 1. Read LEGAL_CORPUS_IMPORT_LIST.md
# 2. Download each document to raw/ subdirectories
# 3. Log downloads to logs/download_log.csv
# 4. Record manifest entries in manifests/download_manifest.csv
```

### Running Chroma Ingestion

To index downloaded documents into ChromaDB for semantic search:

```bash
# Ingest documents into Chroma vector database
python scripts/ingest_chromadb.py \
  --manifest manifests/download_manifest.csv \
  --db-dir indexes/chromadb

# This will:
# 1. Read all documents with status=success from manifest
# 2. Extract text (supports .md, .pdf, .html, .json, .xml)
# 3. Chunk text (1500 chars per chunk, 200 char overlap)
# 4. Generate embeddings (using Chroma's default embedding)
# 5. Store vectors with metadata in indexes/chromadb/
```

## Corpus Structure

### Raw Documents (`raw/`)

```
raw/
├── uk/                    # United Kingdom legislation (P0: COMPLETE)
│   ├── employment/        # Employment law
│   │   └── Employment_Rights_Act_1996.md
│   ├── ip/                # Intellectual property
│   │   ├── Patents_Act_1977.md
│   │   ├── Trade_Secrets_Enforcement_Regulations_2018.md
│   │   └── Copyright_Rights_Databases_Regulations_1997.md
│   └── tax/               # Tax & IR35 regulations
│       └── Social_Security_Intermediaries_Regulations_2000.md
├── us_federal/            # US federal statutes and regulations
├── us_state/              # State-level law (CA, NY, TX, etc.)
├── eu/                    # EU directives and regulations
├── germany/               # German civil code (BGB)
├── france/                # French labor and IP law
├── canada/                # Canadian federal and provincial law
├── australia/             # Australian legislation
├── datasets/              # Pre-labeled contract datasets (CUAD, etc.)
├── caselaw/               # Landmark cases (CourtListener, etc.)
└── industry/              # Industry standards (AIGA, GAG, IGDA, etc.)
```

### Manifest & Logs (`manifests/` and `logs/`)

- **manifests/download_manifest.csv** - Complete inventory with download status, file sizes, and SHA-256 hashes
- **logs/download_log.csv** - Timestamped download operations

### Vector Database (`indexes/chromadb/`)

- **Chroma persistent storage** - 5,290 vectors from all ingested documents
- Collection name: `if_legal_corpus`
- Metadata per vector: `inventory_path`, `document_name`, `local_path`, `sha256`

## UK P0 Documents - Integration Complete

All 5 critical UK documents for freelancer contract analysis have been integrated (2025-11-28):

| Document | Category | Size | Vectors | Status |
| --- | --- | --- | --- | --- |
| Employment Rights Act 1996 | Employment law | 1,031 KB | 6 | ✓ Complete |
| Patents Act 1977 | IP law | 455 KB | 3 | ✓ Complete |
| Trade Secrets Enforcement Regulations 2018 | IP law | 18 KB | 1 | ✓ Complete |
| Social Security (Intermediaries) Regulations 2000 | IR35 Tax | 19 KB | 1 | ✓ Complete |
| Database Rights Regulations 1997 | IP law | 18 KB | 1 | ✓ Complete |

**Total UK collection:** 12 documents, 12+ vectors, 16 MB

## Corpus Coverage Summary

- **Total Inventory Items:** 153
- **Successfully Downloaded:** 91 (59%)
- **Download Errors:** 45 (29%)
- **No Direct Link:** 17 (11%)
- **Chroma Vectors:** 5,290
- **Raw Size:** ~16 MB

## Important Notes

### Chroma Database Size
The ChromaDB indexes are large and should not be committed to git:
- Add `indexes/chromadb/` to `.gitignore`
- Regenerate vectors locally using `scripts/ingest_chromadb.py`

### Virtual Environment
The `.venv/` directory is excluded from git. Install dependencies locally after cloning.

### Document Formats Supported
- Markdown (`.md`)
- PDF (`.pdf`)
- HTML (`.html`)
- XML (`.xml`)
- JSON (`.json`)
- Plain text

### Chunking Strategy
- Default chunk size: 1,500 characters
- Overlap: 200 characters
- Configurable in `scripts/ingest_chromadb.py` via `chunk_text()` function

## License & Attribution

This corpus includes:
- **Public domain legislation** from UK, US, EU, Canada, Australia
- **Creative commons licensed** industry standards (AIGA, GAG, IGDA)
- **Dataset acknowledgments:** CUAD, ContractNLI, LEDGAR

See individual source documents for their specific licensing terms.