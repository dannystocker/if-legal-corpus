# ContractGuard Legal Corpus Import List
## Complete Document Inventory for Chroma Vector Database

**Generated:** 2025-11-27
**Purpose:** Define all legal documents to download and index for contract analysis AI
**Target:** Self-hosted Chroma vector database

---

## Table of Contents

1. [Summary Statistics](#summary-statistics)
2. [Priority Legend](#priority-legend)
3. [US Federal Law](#1-us-federal-law)
4. [US State Law](#2-us-state-law)
5. [European Union](#3-european-union)
6. [Germany](#4-germany)
7. [France](#5-france)
8. [Canada](#6-canada)
9. [Australia](#7-australia)
10. [United Kingdom](#8-united-kingdom)
11. [Contract Datasets](#9-contract-datasets-pre-labeled)
12. [Case Law](#10-landmark-case-law)
13. [Industry Standards](#11-industry-standards)
14. [Download Scripts Reference](#12-download-scripts-reference)

---

## Summary Statistics

| Category | Document Count | Est. Size | Priority P0 |
|----------|---------------|-----------|-------------|
| US Federal | 15 | ~50MB | 8 |
| US State | 24 | ~30MB | 6 |
| EU Directives/Regs | 10 | ~20MB | 6 |
| Germany (BGB) | 6 | ~15MB | 4 |
| France | 4 | ~10MB | 2 |
| Canada | 10 | ~15MB | 5 |
| Australia | 6 | ~10MB | 3 |
| UK | 8 | ~12MB | 5 |
| Datasets (CUAD etc) | 3 | ~500MB | 3 |
| Case Law | 25 | ~100MB | 10 |
| Industry Standards | 12 | ~20MB | 6 |
| **TOTAL** | **~123 sources** | **~780MB** | **58** |

---

## Priority Legend

| Priority | Meaning | Action |
|----------|---------|--------|
| **P0** | Critical - Must have for MVP | Import immediately |
| **P1** | Important - Should have | Import in Phase 2 |
| **P2** | Supplementary - Nice to have | Import in Phase 3 |

---

## 1. US FEDERAL LAW

### 1.1 US Code Titles

| Document | Title | Source | Format | URL | Priority |
|----------|-------|--------|--------|-----|----------|
| **17 USC** | Copyright | House.gov | XML | https://uscode.house.gov/download/download.shtml | **P0** |
| **35 USC** | Patents | House.gov | XML | https://uscode.house.gov/download/download.shtml | **P0** |
| **18 USC Ch.63** | Mail/Wire Fraud | House.gov | XML | https://uscode.house.gov/download/download.shtml | P1 |
| **15 USC §1681** | Fair Credit Reporting | FTC | PDF | https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act | P1 |
| **15 USC §6801** | Gramm-Leach-Bliley | FTC | PDF | https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act | P1 |

### 1.2 Code of Federal Regulations

| Document | Title | Source | Format | URL | Priority |
|----------|-------|--------|--------|-----|----------|
| **29 CFR** | Labor | eCFR | XML | https://www.ecfr.gov/current/title-29 | **P0** |
| **37 CFR** | Patents/Trademarks/Copyright | eCFR | XML | https://www.ecfr.gov/current/title-37 | **P0** |
| **16 CFR Part 310** | Telemarketing Sales | FTC | XML | https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-310 | P1 |
| **16 CFR Part 314** | Safeguards Rule | FTC | XML | https://www.ecfr.gov/current/title-16/part-314 | P1 |

### 1.3 Named Federal Statutes

| Document | Citation | Source | Format | URL | Priority |
|----------|----------|--------|--------|-----|----------|
| **Defend Trade Secrets Act** | 18 USC §1836 | Congress.gov | PDF | https://www.congress.gov/114/plaws/publ153/PLAW-114publ153.pdf | **P0** |
| **Work-for-Hire Definition** | 17 USC §101 | Copyright Office | HTML | https://www.copyright.gov/title17/ | **P0** |
| **Copyright Ownership** | 17 USC §201 | Copyright Office | HTML | https://www.copyright.gov/title17/ | **P0** |
| **FTC Non-Compete Rule** | 2024 Rule | Federal Register | PDF | https://www.federalregister.gov/documents/2024/05/07/2024-09171/non-compete-clause-rule | P1 |
| **ADA Title I** | 42 USC §12101 | EEOC | PDF | https://www.eeoc.gov/statutes/titles-i-and-v-americans-disabilities-act-1990-ada | P2 |

### 1.4 Bulk Download Sources

| Source | Coverage | API | URL |
|--------|----------|-----|-----|
| **GovInfo Bulk Data** | All USC, CFR | REST | https://www.govinfo.gov/bulkdata/ |
| **eCFR API v1** | Current CFR | REST/JSON | https://www.ecfr.gov/developers/documentation/api/v1 |
| **House.gov Download** | US Code by Title | XML/PDF | https://uscode.house.gov/download/download.shtml |
| **Congress.gov** | Bills, Laws | REST | https://www.congress.gov/help/using-data-offsite |

---

## 2. US STATE LAW

### 2.1 California (P0 - Most Restrictive)

| Document | Citation | Key Sections | URL | Priority |
|----------|----------|--------------|-----|----------|
| **Non-Compete Ban** | BPC §16600 | §16600, §16600.1, §16600.5 | https://law.justia.com/codes/california/code-bpc/ | **P0** |
| **Freelance Worker Protection Act** | BPC §18100+ | SB 988 (eff. 1/1/25) | https://leginfo.legislature.ca.gov/ | **P0** |
| **ABC Test (IC Classification)** | Labor Code §2775 | AB 5 provisions | https://leginfo.legislature.ca.gov/ | **P0** |
| **SILENCED Act** | CCP §1001 | SB 331 | https://leginfo.legislature.ca.gov/ | P1 |
| **CCPA/CPRA** | Civ. Code §1798.100 | Data processing | https://oag.ca.gov/privacy/ccpa | P1 |

### 2.2 New York (P0 - Freelancer Protections)

| Document | Citation | Key Sections | URL | Priority |
|----------|----------|--------------|-----|----------|
| **Freelance Isn't Free Act (State)** | GBL Art. 44-A | Labor Law §191-d | https://dol.ny.gov/freelance-isnt-free-act | **P0** |
| **Freelance Isn't Free Act (NYC)** | NYC Admin Code Title 20 | Local Law 140 | https://www.nyc.gov/site/dca/about/freelance-isnt-free-act.page | **P0** |
| **Non-Compete Standards** | Gen. Oblig. Law §510-512 | Common law tests | https://www.nysenate.gov/legislation/laws/GOB | P1 |

### 2.3 Texas (P1 - Employer-Friendly)

| Document | Citation | Key Sections | URL | Priority |
|----------|----------|--------------|-----|----------|
| **Non-Compete Enforceability** | BCC §15.50 | §15.50-15.52 | https://codes.findlaw.com/tx/business-and-commerce-code/ | P1 |
| **Healthcare Non-Compete** | BCC §15.501 | SB 1318 (eff. 9/1/25) | https://capitol.texas.gov/ | P1 |

### 2.4 Delaware (P1 - Governing Law Choice)

| Document | Citation | Key Sections | URL | Priority |
|----------|----------|--------------|-----|----------|
| **Choice of Law** | Del. Code Title 6 §2708 | Contract choice-of-law | https://delcode.delaware.gov/title6/ | P1 |
| **Contract Law** | Del. Code Title 6 Ch.27 | General contracts | https://delcode.delaware.gov/title6/c027/ | P1 |

### 2.5 Other Key States

| State | Document | Citation | Key Issue | Priority |
|-------|----------|----------|-----------|----------|
| **Colorado** | Restrictive Covenant Law | CRS §8-2-113 | $101K+ threshold | P1 |
| **Illinois** | Freedom to Work Act | 820 ILCS 90 | $75K threshold | P1 |
| **Washington** | Non-Compete Law | RCW 49.62 | $250K IC threshold | **P0** |
| **Florida** | Non-Compete + CHOICE Act | Fla. Stat. §542.335 | 4-year expansion | P2 |
| **Massachusetts** | ABC Test | MGL c.149 §148B | Strict IC classification | P1 |
| **Minnesota** | Non-Compete Ban | Near-total ban | Similar to CA | P2 |
| **Oklahoma** | Non-Compete Ban | Near-total ban | Similar to CA | P2 |
| **North Dakota** | Non-Compete Ban | Near-total ban | Similar to CA | P2 |

---

## 3. EUROPEAN UNION

### 3.1 EU Directives

| Document | CELEX ID | Subject | EUR-Lex URL | Priority |
|----------|----------|---------|-------------|----------|
| **Transparent Working Conditions** | 32019L1152 | Worker rights baseline | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L1152 | **P0** |
| **Platform Workers Directive** | 32024L2831 | Gig economy status | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32024L2831 | **P0** |
| **Copyright Directive** | 32019L0790 | IP ownership | https://eur-lex.europa.eu/eli/dir/2019/790/oj | **P0** |
| **Trade Secrets Directive** | 32016L0943 | Confidentiality | https://eur-lex.europa.eu/eli/dir/2016/943/oj | **P0** |
| **GDPR** | 32016R0679 | Data processing | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02016R0679-20160504 | **P0** |
| **Rental/Lending Rights** | 32006L0115 | IP licensing | https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex:32006L0115 | P1 |
| **OSH Framework** | 31989L0391 | Health & safety | https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex:31989L0391 | P2 |

### 3.2 EU Regulations

| Document | CELEX ID | Subject | EUR-Lex URL | Priority |
|----------|----------|---------|-------------|----------|
| **Digital Services Act** | 32022R2065 | Platform obligations | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2065 | P1 |
| **EU AI Act** | 32024R1689 | AI training rights | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | **P0** |

---

## 4. GERMANY

### 4.1 Bürgerliches Gesetzbuch (BGB - Civil Code)

| Section | Subject | English Available | URL | Priority |
|---------|---------|-------------------|-----|----------|
| **§611 et seq.** | Service Contract (Dienstvertrag) | Yes | https://www.gesetze-im-internet.de/englisch_bgb/ | **P0** |
| **§631 et seq.** | Work Contract (Werkvertrag) | Yes | https://www.gesetze-im-internet.de/englisch_bgb/ | **P0** |
| **§611a** | Employee vs Self-Employed | Yes | https://www.gesetze-im-internet.de/englisch_bgb/ | **P0** |
| **§705 et seq.** | Partnership (GbR) | Yes | https://www.gesetze-im-internet.de/englisch_bgb/ | P1 |
| **§14** | Entrepreneur Definition | Yes | https://www.gesetze-im-internet.de/englisch_bgb/ | **P0** |

### 4.2 Other German Law

| Document | Subject | URL | Priority |
|----------|---------|-----|----------|
| **UWG (Unfair Competition)** | Business practices | https://www.gesetze-im-internet.de/englisch_uwg/ | P1 |
| **SGB IV §7** | Social security classification | German law database | P1 |

---

## 5. FRANCE

### 5.1 Code du Travail (Labor Code)

| Article | Subject | URL | Priority |
|---------|---------|-----|----------|
| **L1221-6, L1221-19** | Recruitment, trial periods | https://www.legifrance.gouv.fr/codes/ | P1 |
| **L1222-1, L1222-9** | Good faith, remote work | https://www.legifrance.gouv.fr/codes/ | P1 |

### 5.2 Code de la Propriété Intellectuelle

| Article | Subject | URL | Priority |
|---------|---------|-----|----------|
| **L.111-1** | Copyright ownership default | https://www.legifrance.gouv.fr/ | **P0** |
| **D132-28, D132-29** | Freelance photographer rates | https://www.legifrance.gouv.fr/ | P2 |
| **Part 2** | Industrial property | WIPO Lex | **P0** |

---

## 6. CANADA

### 6.1 Federal Legislation

| Document | Citation | Source | URL | Priority |
|----------|----------|--------|-----|----------|
| **Copyright Act** | RSC 1985, c C-42 | Justice Canada | https://laws-lois.justice.gc.ca/eng/acts/C-42/ | **P0** |
| **Competition Act** | RSC 1985, c C-34 | Justice Canada | https://laws.justice.gc.ca/eng/acts/C-34/ | P1 |
| **Canada Labour Code** | RSC 1985, c L-2 | CanLII | https://www.canlii.org/en/ca/laws/stat/rsc-1985-c-l-2/ | P1 |
| **PIPEDA** | SC 2000, c 5 | Privacy Commissioner | https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/ | **P0** |
| **Employment Insurance Act** | SC 1996, c 23 | CanLII | https://www.canlii.org/en/ca/laws/stat/sc-1996-c-23/ | P1 |
| **Employment Equity Act** | SC 1995, c 44 | CanLII | https://www.canlii.org/en/ca/laws/stat/sc-1995-c-44/ | P2 |

### 6.2 Provincial Legislation

| Province | Document | Citation | URL | Priority |
|----------|----------|----------|-----|----------|
| **Ontario** | Employment Standards Act | O. Reg. 435/07 | https://www.ontario.ca/laws/statute/00e41 | **P0** |
| **BC** | Employment Standards Act | RSBC 1996, c 113 | BC Legislature | **P0** |
| **Quebec** | Labour Standards Act | CQLR c N-1.1 | https://www.canlii.org/en/qc/laws/stat/cqlr-c-n-1.1/ | **P0** |

---

## 7. AUSTRALIA

### 7.1 Federal Legislation

| Document | Citation | Source | URL | Priority |
|----------|----------|--------|-----|----------|
| **Fair Work Act 2009** | Cth | Fair Work | https://www.fairwork.gov.au/about-us/legislation | **P0** |
| **Independent Contractors Act 2006** | Act No. 162 | Legislation.gov.au | https://www.legislation.gov.au/Series/C2006A00162 | **P0** |
| **Copyright Act 1968** | Cth | AustLII | https://www7.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/ | **P0** |
| **Competition and Consumer Act 2010** | Cth | Legislation.gov.au | https://www.legislation.gov.au/C2004A00109/latest | P1 |
| **Privacy Act 1988** | Cth | AustLII | https://www7.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/ | P1 |
| **Australian Consumer Law** | Part II CCA | Legislation.gov.au | https://www.legislation.gov.au/C2004A00109/latest | P1 |

---

## 8. UNITED KINGDOM

### 8.1 Acts of Parliament

| Document | Citation | Source | URL | Priority |
|----------|----------|--------|-----|----------|
| **Employment Rights Act 1996** | c. 18 | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/1996/18/contents | **P0** |
| **Copyright, Designs and Patents Act 1988** | c. 48 | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/1988/48 | **P0** |
| **Patents Act 1977** | c. 37 | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/1977/37 | P1 |
| **Trade Secrets Regulations 2018** | SI 2018/597 | legislation.gov.uk | https://www.legislation.gov.uk/uksi/2018/597/made | **P0** |

### 8.2 IR35 (Off-Payroll Working)

| Document | Citation | Source | URL | Priority |
|----------|----------|--------|-----|----------|
| **Social Security (Intermediaries) Regs** | SI 2000/727 | legislation.gov.uk | https://www.legislation.gov.uk/uksi/2000/727 | **P0** |
| **ITEPA 2003 Part 2 Ch.8** | c. 1 | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/2003/1 | **P0** |
| **Database Rights Regs 1997** | SI 1997/3032 | legislation.gov.uk | https://www.legislation.gov.uk/uksi/1997/3032 | P2 |

---

## 9. CONTRACT DATASETS (Pre-Labeled)

### 9.1 Primary Training Data

| Dataset | Description | Size | Source | Priority |
|---------|-------------|------|--------|----------|
| **CUAD** | 13K+ labeled clause annotations, 510 contracts, 41 clause types | ~500MB | https://www.atticusprojectai.org/cuad | **P0** |
| **ContractNLI** | Natural language inference for contracts | ~50MB | Stanford NLP | **P0** |
| **LEDGAR** | SEC filing provisions, corporate baseline | ~200MB | HuggingFace | **P0** |

### 9.2 CUAD Clause Types (41 Total)

**Critical for Freelancers (Import First):**
- Governing Law
- Non-Compete
- Exclusivity
- IP Ownership Assignment
- License Grant
- Non-Disparagement
- Termination For Convenience
- Limitation Of Liability
- Indemnification
- Insurance
- Cap On Liability
- Uncapped Liability
- Warranty Duration
- Post-Termination Services

---

## 10. LANDMARK CASE LAW

### 10.1 Non-Compete Cases

| Case | Citation | Jurisdiction | Year | Key Test | Priority |
|------|----------|--------------|------|----------|----------|
| **PepsiCo v. Redmond** | 54 F.3d 1262 | 7th Cir. | 1995 | Inevitable disclosure | **P0** |
| **Mitchell v. Reynolds** | Common Law | England | 1711 | Reasonableness framework | **P0** |
| **Oregon Steam v. Winsor** | 87 U.S. 564 | SCOTUS | 1874 | Ancillary to sale | P1 |
| **Ryan v. FTC** | 5th Cir. 2024 | 5th Cir. | 2024 | FTC authority limits | P1 |

### 10.2 IP / Work-for-Hire Cases

| Case | Citation | Jurisdiction | Year | Key Test | Priority |
|------|----------|--------------|------|----------|----------|
| **CCNV v. Reid** | 490 U.S. 730 | SCOTUS | 1989 | 12-factor agency test | **P0** |
| **Dubilier Condenser** | 289 U.S. 178 | SCOTUS | 1933 | Hired-to-invent doctrine | P1 |
| **SCA Hygiene v. First Quality** | 580 U.S. 557 | SCOTUS | 2017 | Patent damages limits | P2 |

### 10.3 Indemnification Cases

| Case | Citation | Jurisdiction | Year | Key Test | Priority |
|------|----------|--------------|------|----------|----------|
| **Brooks v. Judlau** | 11 NY3d 204 | NY | 2008 | Comparative negligence | **P0** |
| **Santa Barbara v. Superior Court** | 41 Cal.4th 747 | CA | 2007 | Gross negligence exception | **P0** |
| **Steamfitters v. Erie Insurance** | 233 A.3d 59 | MD | 2020 | Clear/unequivocal standard | P1 |

### 10.4 Arbitration Cases

| Case | Citation | Jurisdiction | Year | Key Test | Priority |
|------|----------|--------------|------|----------|----------|
| **Epic Systems v. Lewis** | 584 U.S. ___ | SCOTUS | 2018 | FAA enforcement | **P0** |
| **Mastrobuono v. Shearson** | 514 U.S. 52 | SCOTUS | 1995 | Choice-of-law vs arbitration | **P0** |
| **Pinnacle v. Pinnacle Market** | 55 Cal.4th 223 | CA | 2012 | Unconscionability 2-prong | **P0** |

### 10.5 Trade Secrets / NDA Cases

| Case | Citation | Jurisdiction | Year | Key Test | Priority |
|------|----------|--------------|------|----------|----------|
| **Silicon Image v. Analogk** | N.D. Cal. | N.D. Cal. | 2008 | NDA expiration effects | P1 |
| **Hamilton v. Juul Labs** | N.D. Cal. | N.D. Cal. | 2021 | Overbreadth analysis | P1 |
| **Gordon v. Landau** | 49 Cal.2d 212 | CA | 1958 | CA §16600 trade secret exception | P1 |

### 10.6 Moral Rights Cases

| Case | Citation | Jurisdiction | Year | Key Test | Priority |
|------|----------|--------------|------|----------|----------|
| **Gilliam v. ABC** | 538 F.2d 14 | 2d Cir. | 1976 | Integrity/mutilation test | **P0** |
| **Frisby v. BBC** | UK Court | UK | - | Contractual moral rights | P1 |
| **Confetti Records v. Warner** | UK Court | UK | - | CDPA 1988 requirements | P1 |

---

## 11. INDUSTRY STANDARDS

### 11.1 Gaming Industry

| Standard | Organization | URL | Priority |
|----------|--------------|-----|----------|
| **Steam Distribution Agreement** | Valve | https://store.steampowered.com | **P0** |
| **Epic Games Store Agreement** | Epic | https://dev.epicgames.com/docs/epic-games-store/agreements | **P0** |
| **PlayStation GDPA** | Sony | SEC Filings | P1 |
| **Xbox Publisher License** | Microsoft | SEC Filings | P1 |
| **IGDA Contract Walk-Through** | IGDA | https://igda.org/resourcelibrary/game-industry-standards/ | **P0** |
| **IGDA Crediting Guidelines** | IGDA | https://igda.org/ | P1 |

### 11.2 Entertainment

| Standard | Organization | URL | Priority |
|----------|--------------|-----|----------|
| **SAG-AFTRA 2025 Commercials** | SAG-AFTRA | https://www.sagaftra.org/ | **P0** |
| **SAG-AFTRA Video Game Agreement** | SAG-AFTRA | https://www.sagaftra.org/production-center/contract/802/ | **P0** |
| **WGA Minimum Basic Agreement** | WGA | https://www.wga.org/contracts/contracts/schedule-of-minimums | **P0** |

### 11.3 Creative Services

| Standard | Organization | URL | Priority |
|----------|--------------|-----|----------|
| **AIGA Standard Agreement** | AIGA | https://www.aiga.org/resources/aiga-standard-form-of-agreement-for-design-services | **P0** |
| **GAG Handbook (17th Ed)** | Graphic Artists Guild | https://graphicartistsguild.org/ | **P0** |
| **Photography Licensing Standards** | Various | https://www.pixsy.com/image-licensing/photo-licensing-agreement | P1 |

### 11.4 Tech/Software

| Standard | Organization | URL | Priority |
|----------|--------------|-----|----------|
| **Open Source Licenses** | OSI | https://opensource.org/licenses | P1 |
| **MIT License** | OSI | https://opensource.org/license/mit | P1 |
| **Apache 2.0** | Apache | https://www.apache.org/licenses/LICENSE-2.0 | P1 |
| **GPL v3** | GNU | https://www.gnu.org/licenses/gpl-3.0.en.html | P1 |

---

## 12. DOWNLOAD SCRIPTS REFERENCE

All download scripts are in: `/home/setup/CLOUD_SESSION_LEGAL_DB_BUILD.md`

### Script Mapping

| Script | Data Source | Output Directory |
|--------|-------------|------------------|
| `download_cuad.py` | CUAD Dataset | `raw/cuad/` |
| `download_us_federal.py` | GovInfo API | `raw/us_federal/` |
| `download_us_caselaw.py` | CourtListener | `raw/us_caselaw/` |
| `download_eu_law.py` | EUR-Lex SPARQL | `raw/eu_law/` |
| `download_canada_law.py` | CanLII | `raw/canada_law/` |
| `download_australia_law.py` | AustLII | `raw/australia_law/` |

### Execution Order

```bash
# Phase 1: Datasets (Highest Value)
python scripts/download_cuad.py

# Phase 2: US Federal
export GOVINFO_API_KEY="your_key"
python scripts/download_us_federal.py
python scripts/download_us_caselaw.py

# Phase 3: International
python scripts/download_eu_law.py
python scripts/download_canada_law.py
python scripts/download_australia_law.py

# Phase 4: Process & Index
python scripts/process_cuad.py
python scripts/process_documents.py
python scripts/embed_and_index.py
```

---

## Chroma Collection Structure

After import, Chroma will have these collections:

```
chroma_db/
├── contract_clauses      # CUAD labeled clauses (P0)
├── us_federal_law        # USC, CFR (P0)
├── us_state_law          # CA, NY, TX, etc. (P0)
├── us_case_law           # CourtListener opinions (P1)
├── eu_directives         # EUR-Lex (P0)
├── eu_regulations        # GDPR, AI Act, DSA (P0)
├── germany_bgb           # Civil Code (P0)
├── france_code           # Labor, IP codes (P1)
├── canada_federal        # Copyright, PIPEDA (P0)
├── canada_provincial     # ON, BC, QC employment (P0)
├── australia_federal     # Fair Work, Copyright (P0)
├── uk_legislation        # ERA, CDPA, IR35 (P0)
└── industry_standards    # AIGA, GAG, IGDA (P1)
```

---

## Estimated Totals

| Metric | Value |
|--------|-------|
| **Total Documents** | ~123 sources |
| **Total Raw Size** | ~780MB |
| **Processed Chunks** | ~500K vectors |
| **Chroma DB Size** | ~1-2GB |
| **P0 Documents** | 58 (must have) |
| **Download Time** | 4-6 hours |
| **Processing Time** | 2-3 hours |
| **Embedding Time** | 1-2 hours (CPU) |

---

## Next Steps

1. Execute `CLOUD_SESSION_LEGAL_DB_BUILD.md` to download and index
2. Validate with test queries
3. Build contract analysis prompts using RAG
4. Integrate with upload pipeline

---

*Generated by IF.optimise Haiku swarm research*
*6 parallel agents, ~15 minutes total research time*
