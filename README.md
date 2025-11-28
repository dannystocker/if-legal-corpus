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

## IF.TTT Compliance (Traceable, Transparent, Trustworthy)

This legal corpus implements the IF.TTT framework for legal service compliance:

### Traceable
Every document has:
- Unique citation ID: `if://citation/[uuid]` format
- SHA-256 cryptographic hash for integrity verification
- Git commit reference showing when added to repository
- Complete provenance chain from source through ingestion

**Access citations:**
```bash
# View all citations with metadata
cat citations/legal-corpus-citations-2025-11-28.json | jq '.[].citation_id'

# Search for specific document
grep "Employment Rights Act" citations/legal-corpus-citations-2025-11-28.json
```

### Transparent
Full audit trail available:
- **Citation Schema:** `schemas/legal-citation-v1.0.json` - JSON schema defining all required fields
- **Citation Records:** `citations/legal-corpus-citations-2025-11-28.json` - 59 documents with metadata
- **Provenance Audit:** `audit/PROVENANCE_CHAIN.md` - Complete chain of custody documentation
- **Validation Reports:** `audit/validation-report-*.json` - Automated verification results

### Trustworthy
All documents verified:
- Downloaded from authoritative government sources
- Hash-verified against original files
- Ingested into Chroma with citation metadata preserved
- Automated validation tool checks integrity: `python tools/validate_legal_citations.py`

**Current Verification Status:**
```
RESULT: ALL 59 CITATIONS VERIFIED (100%)
  ✓ Schema validation: 59/59
  ✓ File existence: 59/59
  ✓ SHA-256 hash verification: 59/59
  ✓ Provenance chain: 59/59
```

### Citation Validation

To validate all citations against schema and verify file integrity:

```bash
# Activate virtual environment
source .venv/bin/activate

# Run validation tool
python tools/validate_legal_citations.py
```

This validates:
1. JSON schema compliance
2. Citation ID format (if://citation/[uuid])
3. File existence and accessibility
4. SHA-256 hash integrity
5. File size consistency
6. Git commit references
7. Complete provenance chains
8. Timestamp validity

### Using Citations in Legal Services

For ContractGuard or other legal services using this corpus:

1. **Preserve Metadata**: When retrieving documents via Chroma, extract full citation metadata
2. **Display Sources**: Always show `authoritative_source.url` to users
3. **Show Verification**: Display `verification_date` and `citation_status`
4. **Include Disclaimer**: Add legal disclaimer on analysis pages:
   ```
   Legal Disclaimer: This information is for reference only and does not constitute
   legal advice. All legal analysis should be reviewed by qualified legal counsel.
   Consult current official sources for critical decisions.
   ```
5. **Maintain Audit Log**: Record which citations were used for each contract analysis

### Example Citation Record

Every document includes complete metadata:

```json
{
  "citation_id": "if://citation/5f2c229f-58d2-4ad1-b431-4db4459a2213",
  "citation_type": "legal_statute",
  "document_name": "Employment Rights Act 1996",
  "jurisdiction": "UK",
  "authoritative_source": {
    "url": "https://www.legislation.gov.uk/ukpga/1996/18/contents",
    "accessed_date": "2025-11-28T04:18:00Z",
    "verification_method": "sha256_hash",
    "source_type": "government_website"
  },
  "local_verification": {
    "local_path": "raw/uk/employment-rights-act-1996",
    "sha256": "f72b8ed35ee46f25acf84bb8263298d61644e932dae0907290372cffbda0f892",
    "file_size_bytes": 234794,
    "ingested_date": "2025-11-28T04:13:00Z",
    "git_commit": "57ad645"
  },
  "provenance_chain": [
    {
      "step": "download",
      "agent": "legal-corpus-downloader-v1.0",
      "timestamp": "2025-11-28T04:11:52Z",
      "verification": "Downloaded from https://www.legislation.gov.uk/..."
    },
    {
      "step": "validation",
      "agent": "legal-corpus-validator-v1.0",
      "timestamp": "2025-11-28T04:12:15Z",
      "verification": "SHA-256 hash verified"
    },
    {
      "step": "ingestion",
      "agent": "chromadb-pipeline-v1.0",
      "timestamp": "2025-11-28T04:13:00Z",
      "verification": "Stored in Chroma vector database"
    }
  ],
  "citation_status": "verified",
  "verification_date": "2025-11-28T04:19:00Z",
  "verifier": "if-legal-corpus-pipeline-v1.0"
}
```

### Corpus Statistics by Jurisdiction

**Total Documents Verified:** 59

| Jurisdiction | Count | Status |
|---|---|---|
| UK | 7 | verified |
| US | 21 | verified |
| Canada | 8 | verified |
| Australia | 6 | verified |
| Germany | 5 | verified |
| EU | 1 | verified |
| Industry/International | 11 | verified |

### File Locations

- **Schema:** `/home/setup/if-legal-corpus/schemas/legal-citation-v1.0.json`
- **Citations:** `/home/setup/if-legal-corpus/citations/legal-corpus-citations-2025-11-28.json`
- **Audit Trail:** `/home/setup/if-legal-corpus/audit/PROVENANCE_CHAIN.md`
- **Validation Tool:** `/home/setup/if-legal-corpus/tools/validate_legal_citations.py`
- **Validation Reports:** `/home/setup/if-legal-corpus/audit/validation-report-*.json`

## License & Attribution

This corpus includes:
- **Public domain legislation** from UK, US, EU, Canada, Australia
- **Creative commons licensed** industry standards (AIGA, GAG, IGDA)
- **Dataset acknowledgments:** CUAD, ContractNLI, LEDGAR

See individual source documents and audit trail for their specific licensing terms and source attribution.