# Legal Corpus Roadmap

This roadmap tracks coverage of the inventory listed in `LEGAL_CORPUS_IMPORT_LIST.md`.

| inventory_path | document_name | download_status | index_status | notes |
| --- | --- | --- | --- | --- |
| inventory_file | LEGAL_CORPUS_IMPORT_LIST.md | planned | not_started | Inventory present; run `scripts/download_all.py` to populate manifest and start downloads. |

## Unable to download — reasons and workarounds
- Items without direct URLs (for example, some case law rows) will be marked `no_direct_link` in the manifest. Extend the downloader to use CourtListener or other APIs by citation to automate these where possible.

