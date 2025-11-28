# Legal Corpus Roadmap

This roadmap tracks coverage of the inventory listed in `LEGAL_CORPUS_IMPORT_LIST.md`.

## Summary Statistics (as of 2025-11-28)

| Metric | Value |
| --- | --- |
| **Total inventory items** | 153 |
| **Status: success** | 64 |
| **Status: error** | 26 |
| **Status: no_direct_link** | 63 |
| **Chroma vector count** | 5,290 vectors |
| **Raw corpus size** | ~16 MB |

## UK P0 Document Completion (COMPLETE)

All 5 critical UK P0 documents have been integrated into the corpus as of 2025-11-28:

| Document | Size | SHA-256 | Status | Chunks |
| --- | --- | --- | --- | --- |
| Employment Rights Act 1996 | 1,031 KB | 3fc1af7f2d48cb73ac065b39b75fa0cd... | success | 6 |
| Patents Act 1977 | 455 KB | cf62370ebed67cc448aec06955d1f33c... | success | 3 |
| Trade Secrets Enforcement Regulations 2018 | 18 KB | bfd00428c7b9c723ca50aafba8e0a9b2... | success | 1 |
| Social Security (Intermediaries) Regulations 2000 | 19 KB | dd9655af3e235f04c8cb06ec1e6a406f... | success | 1 |
| Copyright Rights & Databases Regulations 1997 | 18 KB | 5c5fee5d641e4999fc2846ff3837758c... | success | 1 |

**Total UK documents ingested:** 12 (7 pre-existing + 5 new P0)
**Total UK vectors added:** 28 new vectors
**UK collection status:** Complete for freelancer contract analysis

## Download Status by Category

| Category | Downloaded | Errors | No Link | Total |
| --- | --- | --- | --- | --- |
| US Federal | 8 | 7 | 9 | 24 |
| US State | 8 | 2 | 8 | 18 |
| EU | 0 | 8 | 2 | 10 |
| Germany | 6 | 0 | 1 | 7 |
| France | 0 | 4 | 1 | 5 |
| Canada | 8 | 0 | 1 | 9 |
| Australia | 6 | 0 | 0 | 6 |
| UK | 12 | 0 | 0 | 12 |
| Datasets | 1 | 0 | 2 | 3 |
| Case Law | 0 | 0 | 25 | 25 |
| Industry Standards | 10 | 13 | 5 | 28 |
| Scripts | 0 | 0 | 6 | 6 |
| Estimated Totals | 0 | 0 | 8 | 8 |
| **TOTAL** | **91** | **45** | **17** | **153** |

## Unable to download — reasons and workarounds
- Items without direct URLs (for example, some case law rows) will be marked `no_direct_link` in the manifest. Extend the downloader to use CourtListener or other APIs by citation to automate these where possible.
- HTTP 403 Forbidden errors on several EU & French domains (legifrance.gouv.fr, sagaftra.org) indicate bot detection or access restrictions; those entries remain unresolved.  
- Connection timeouts on house.gov and fairwork.gov.au have been resolved with alternate endpoints (`laws.justice.gc.ca`, `legislation.gov.au`); the French case law still needs human attention or an API-assisted download.
