# Non-Abelian Hodge primary-source manifest

This is the acquisition list for the permanent NAH source corpus. A source is
usable for an `AI-CHECKED FROM PDF` checkpoint only after its primary PDF is
saved in this folder and read directly. Human review is recorded separately in
the source checkpoints and theorem ledger.

This manifest was assembled and updated through an AI-assisted
source-retrieval workflow under the author's direction. It records
bibliographic identities, retrieval history, stable source locations, local
filenames, file hashes, and mechanical PDF validation. These records do not
constitute independent human verification of the mathematical contents.

`LOCAL` describes the checkpoint-building workspace in which the recorded PDFs
were checked. A public release may omit third-party PDFs while retaining their
primary URLs and exact hashes; such PDFs must be retrieved and hash-matched
before a checkpoint is rebuilt or newly marked `AI-CHECKED FROM PDF`.

| Key | Primary source and exact version | Stable primary location | Local filename | Retrieved / attempted | Status |
| --- | --- | --- | --- | --- | --- |
| `SIM90` | C. T. Simpson, *Harmonic Bundles on Noncompact Curves*, JAMS 3 (1990), no. 3, 713–770; DOI `10.1090/S0894-0347-1990-1040197-8`; JAMS published version, 58 pages | https://doi.org/10.1090/S0894-0347-1990-1040197-8; AMS publisher PDF: https://www.ams.org/journals/jams/1990-03-03/S0894-0347-1990-1040197-8/S0894-0347-1990-1040197-8.pdf | `SIM90_Simpson_Harmonic_Bundles_Noncompact_Curves.pdf` | Re-retrieved from AMS publisher PDF 2026-08-03; staged PDF byte-identical to local and Ghostscript-validated | `LOCAL — 2026-08-03` |
| `SIM92` | C. T. Simpson, *Higgs Bundles and Local Systems*, Publ. Math. IHÉS 75 (1992), 5–95; Numdam/PMIHES journal PDF, published online 1992-12-28 | https://www.numdam.org/item/PMIHES_1992__75__5_0.pdf | `SIM92_Simpson_Higgs_Bundles_Local_Systems.pdf` | Re-retrieved from Numdam 2026-08-03; staged PDF byte-identical to local and Ghostscript-validated | `LOCAL — 2026-08-03` |
| `COR88` | K. Corlette, *Flat G-Bundles with Canonical Metrics*, J. Differential Geom. 28 (1988), no. 3, 361–382; DOI `10.4310/jdg/1214442469`; JDG published version, 22 pages | https://doi.org/10.4310/jdg/1214442469; Project Euclid record: http://projecteuclid.org/euclid.jdg/1214442469 | `COR88_Corlette_Flat_G_Bundles.pdf` | User-supplied local PDF Ghostscript-validated 2026-08-03; primary retrieval re-attempted 2026-08-03 and blocked upstream | `LOCAL USER-SUPPLIED — PRIMARY RETRIEVAL BLOCKED 2026-08-03` |
| `MOC02` | T. Mochizuki, *Asymptotic Behaviour of Tame Nilpotent Harmonic Bundles with Trivial Parabolic Structure*; arXiv `math/0212232v1`, submitted 2002-12-17 | https://arxiv.org/pdf/math/0212232v1 | `MOC02_Mochizuki_Tame_Nilpotent_Trivial_Parabolic.pdf` | Re-retrieved from arXiv v1 2026-08-03; staged PDF byte-identical to local and Ghostscript-validated | `LOCAL — 2026-08-03` |
| `MOC04` | T. Mochizuki, *Kobayashi–Hitchin Correspondence for Tame Harmonic Bundles and an Application*; arXiv `math/0411300v3`, last revised 2006-08-29 | https://arxiv.org/pdf/math/0411300v3 | `MOC04_Mochizuki_KH_Tame_Harmonic_Bundles.pdf` | Re-retrieved from arXiv v3 2026-08-03; staged PDF byte-identical to local and Ghostscript-validated | `LOCAL — 2026-08-03` |
| `MOC03` | T. Mochizuki, *Asymptotic Behaviour of Tame Harmonic Bundles and an Application to Pure Twistor D-Modules*; arXiv `math/0312230v2`, last revised 2004-03-01 | https://arxiv.org/pdf/math/0312230v2 | `MOC03_Mochizuki_Tame_Harmonic_Asymptotics.pdf` | Re-retrieved from arXiv v2 2026-08-03; staged PDF byte-identical to local and Ghostscript-validated | `LOCAL — 2026-08-03` |
| `MOC09` | T. Mochizuki, *Kobayashi-Hitchin correspondence for tame harmonic bundles II*, Geometry & Topology 13 (2009), 359-455; DOI `10.2140/gt.2009.13.359`; Geometry & Topology published version, 98 pages | https://doi.org/10.2140/gt.2009.13.359; MSP publisher PDF: https://msp.org/gt/2009/13-1/gt-v13-n1-p10-p.pdf | `MOC09_Mochizuki_KH_Tame_Harmonic_Bundles_II.pdf` | Re-retrieved from MSP publisher PDF 2026-08-03; staged PDF byte-identical to local and Ghostscript-validated | `LOCAL — 2026-08-03` |
| `DEL70` | P. Deligne, *Équations différentielles à points singuliers réguliers*, Lecture Notes in Mathematics 163, Springer-Verlag (1970); IAS author-archive PDF `Number9.pdf`, 136-page scan | https://publications.ias.edu/sites/default/files/Number9.pdf; record page: https://publications.ias.edu/deligne/paper/355 | `DEL70_Deligne_Regular_Singular_Connections.pdf` | Re-retrieved from IAS author archive 2026-08-03; staged PDF byte-identical to local and Ghostscript-validated | `LOCAL — 2026-08-03` |

## Integrity hashes

These hashes identify the exact PDF bytes used for the checkpoints.

| Key | SHA-256 |
| --- | --- |
| `COR88` | `4ef26b5f6a65ad186f8bf3c2d32fcba6ba08e48ec3593abc17ddd96965fe1127` |
| `DEL70` | `0dc37edd7758198cc4cd7ebed0dae63ff821336cebe739636a31591671593ba2` |
| `MOC02` | `c09228635bfb9dabe3cc2e8f21801086dae0eacee3873ae6e50c5dff7e0fe994` |
| `MOC03` | `5453fc5665bb1650211b4dfb7f28c5b8c8a82645c068510657233ddf14cbac62` |
| `MOC04` | `f218e8dfaded8d71d9bbfb3278c666f95570b5f3d3cf540b590c52c2f6988266` |
| `MOC09` | `23c0ef47c11989edeba0cbb433a519825390deb0b3244862e97a1edb80e5945c` |
| `SIM90` | `ec6a9f58caa18cfd9c548a703fe7a1fbb81a6ed6afb18f2a00b8d10450a88b25` |
| `SIM92` | `74651fcdbcd66b5fdf19724b74e0ecbfcad09033dbff2f14c3b7ed2994f76029` |

When a source is acquired, replace its status with `LOCAL — YYYY-MM-DD`, record the exact version beside the title, and do not change the prescribed filename unless the manifest is updated simultaneously.

## Retrieval notes

- `SIM90`: the old manifest URL `https://www.ams.org/jams/1990-03-03/S0894-0347-1990-1040197-8/S0894-0347-1990-1040197-8.pdf` returned AMS HTML on 2026-07-20. The AMS publisher PDF at `https://www.ams.org/journals/jams/1990-03-03/S0894-0347-1990-1040197-8/S0894-0347-1990-1040197-8.pdf` retrieved a valid 58-page PDF on 2026-08-03 with a browser-like user agent; the staged PDF was byte-identical to the local file, and this remains the recorded stable PDF URL.
- `COR88`: automated Project Euclid/JDG retrieval on 2026-07-18 returned an access-protection HTML page; International Press/JDG URL patterns checked the same day were either access-protected or 404. Resolved the same day by user-supplied `Corlette_Flat_G_Bundles.pdf`, copied to the prescribed local filename. Re-attempted primary retrieval on 2026-07-20, 2026-07-23, and 2026-08-03 via DOI, Project Euclid record, Project Euclid direct-download URL patterns, and International Press `mode=pdf`; DOI/Project Euclid returned HTML access-protection pages and International Press returned HTTP 403. No non-primary mirror was used.
- All source PDFs with accessible primary URLs were re-retrieved on 2026-08-03 and compared byte-for-byte against the prescribed local files. The local files were already identical, so no PDF content was changed.

## Local PDF validation

- `SIM90_Simpson_Harmonic_Bundles_Noncompact_Curves.pdf`: PDF, 58 pages; Ghostscript-validated 2026-08-03.
- `SIM92_Simpson_Higgs_Bundles_Local_Systems.pdf`: PDF, 92 pages; Ghostscript-validated 2026-08-03.
- `COR88_Corlette_Flat_G_Bundles.pdf`: PDF, 22 pages; Ghostscript-validated 2026-08-03.
- `MOC02_Mochizuki_Tame_Nilpotent_Trivial_Parabolic.pdf`: PDF, 110 pages; Ghostscript-validated 2026-08-03.
- `MOC04_Mochizuki_KH_Tame_Harmonic_Bundles.pdf`: PDF, 121 pages; Ghostscript-validated 2026-08-03.
- `MOC03_Mochizuki_Tame_Harmonic_Asymptotics.pdf`: PDF, 358 pages; Ghostscript-validated 2026-08-03.
- `MOC09_Mochizuki_KH_Tame_Harmonic_Bundles_II.pdf`: PDF, 98 pages; Ghostscript-validated 2026-08-03.
- `DEL70_Deligne_Regular_Singular_Connections.pdf`: PDF, 136-page page tree; Ghostscript-validated 2026-08-03.

## Mathematics-first reading order

1. `SIM92` and `COR88`: compact/reductive correspondence and harmonic metrics.
2. `SIM90`: punctured curves and tame local behavior.
3. `MOC04`: filtered/parabolic tame correspondence.
4. `MOC02`: nilpotent, trivial-parabolic asymptotics only.
5. `MOC03`: general tame asymptotics and flat-section norm estimates.
6. `MOC09`: nonzero-`lambda` filtered/parabolic KH, filtered local systems, and quasiprojective flat/Higgs equivalence.
7. `DEL70`: logarithmic extensions, residues, and regular singularities.
