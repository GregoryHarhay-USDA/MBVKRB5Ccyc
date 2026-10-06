# MBVKRB5Ccyc: Systems Biology Data Repository for *Mycoplasmopsis bovis* Strain KRB5 (Version 1.0.0)

[![Database Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com/GregoryHarhay-USDA/MBVKRB5Ccyc)
[![License](https://img.shields.io/badge/License-Unlicense-green.svg)](https://github.com/GregoryHarhay-USDA/MBVKRB5Ccyc/blob/main/LICENSE)
[![SCINet Host](https://img.shields.io/badge/USDA_SCINet-Pathway_Tools_v29.5-orange.svg)](https://pathwaytools.scinet.usda.gov/MBVKRB5C/organism-summary)

This repository serves as the official public data archive for **MBVKRB5Ccyc v1.0.0**, a manually curated Pathway/Genome Database (PGDB) and computational genomics framework for the wall-less livestock pathogen ***Mycoplasmopsis bovis*** strain KRB5. 

Developed by researchers at the U.S. Department of Agriculture Agricultural Research Service (USDA-ARS), this platform integrates sequence-domain mapping with 3D structural modeling (AlphaFold2 and Foldseek) and population-scale genomic surveillance across 122 closed complete genomes. The repository houses database flat-files, 3D structural alignment outputs, execution logs, population variant profiles, and epidemiological metadata supporting two manuscripts currently under peer review.

---

## 1. Repository Directory Structure

The repository is organized into distinct, modular directories containing raw and processed dataset files. Top-level directory names match direct download links cited in submitted manuscripts to ensure full backward compatibility and link persistence.

```text
GregoryHarhay-USDA/MBVKRB5Ccyc/
├── README.md                                # Master repository documentation and data guide
├── LICENSE                                  # Unlicense public domain declaration
│
├── PGDB/                                    # [MANUSCRIPT LINK] Pathway/Genome Database flat-files
│   ├── UNCURATED/                           # Baseline automated PathoLogic flat-files (mbvkrb5cyc)
│   └── CURATED/                             # Manually curated v1.0.0 flat-files (MBVKRB5Ccyc)
│
├── foldseek/                                # [MANUSCRIPT LINK] Legacy structural search directory
│   ├── 4X9M.v.KRB5_proteome.html            # Foldseek 3D structural alignment of M. pneumoniae GlpO against KRB5
│   └── README.md                            # Pointer note referencing expanded protein_structures/ directory
│
├── protein_structures/                      # 3D structural models and fold alignments
│   ├── pdb_models/                          # AlphaFold2 PDB structural models (Opd, NoxA, TrxB, PDHc subunits)
│   └── templates/                           # Reference template PDB files (e.g., 4X9M.pdb, 6FZI.pdb)
│
├── ptools-logs/                             # [MANUSCRIPT LINK] Pathway Tools v29.5 run reports
│   ├── UNCURATED_pwy-inference-report_2026-08-05.txt
│   ├── CURATED_pwy-inference-report_2026-08-05.txt
│   ├── UNCURATED_pwy-rescoring-report_2026-08-05.txt
│   ├── CURATED_pwy-rescoring-report_2026-08-25.txt
│   ├── UNCURATED_dead-end-metabolites-2026-08-05_17-47-30.txt
│   ├── CURATED_dead-end-metabolites-2026-08-25_18-23-37.txt
│   ├── UNCURATED_chokepoint-reactions-2026-08-05_17-46-15.txt
│   └── CURATED_chokepoint-reactions-2026-08-25_18-22-29.txt
│
├── metadata/                                # Population surveillance and epidemiological metadata
│   └── clean_m_bovis_119_biosamples_environmental_metadata_filled.csv
│
└── alignments_vcf/                          # Genomic population surveillance and variant profiles
    ├── vcf/                                 # VCF variant calls across 122 closed complete genomes
    ├── msa/                                 # Sequence Alignment/Map (SAM) format files (.sam) for 16 opd genotypes
    └── trees/                               # MrBayes unrooted phylogenetic tree outputs (.nex/.tree)
```

> **Manuscript Link Compatibility Note**: The top-level `foldseek/` folder contains the specific interactive file `4X9M.v.KRB5_proteome.html` explicitly cited in the *Microbiology Spectrum* resource report. Users interested in broader structural modeling files should explore `protein_structures/`.

---

## 2. Dataset Descriptions & Directory Guide

### `PGDB/` — Pathway/Genome Database Flat-Files
Contains complete flat-file exports of the MBVKRB5Ccyc database formatted for direct import into Pathway Tools (v29.5) or computational parsing via BioPython and Perl APIs.
* **`UNCURATED/`**: The automated PathoLogic baseline build (`mbvkrb5cyc`), generated prior to manual structural curation. Accessible online at the [MBVKRB5 Uncurated PGDB](https://pathwaytools.scinet.usda.gov/organism-summary?object=MBVKRB5).
* **`CURATED/`**: The refined v1.0.0 database (`MBVKRB5Ccyc`), incorporating 61 defined pathways, 444 reactions, 195 annotated enzymes, and 139 cytosolic chokepoint targets. Accessible online at the [MBVKRB5Ccyc Curated PGDB](https://pathwaytools.scinet.usda.gov/MBVKRB5C/organism-summary).

### `foldseek/` & `protein_structures/` — Structural Bioinformatic Outputs
Contains predicted 3D protein structures generated using AlphaFold2 (ColabFold v1.5.5) and tertiary fold comparison alignments generated using Foldseek.
* **`4X9M.v.KRB5_proteome.html`**: An interactive Foldseek alignment report comparing the crystal structure of *Mycoplasmoides pneumoniae* glycerol-3-phosphate oxidase (GlpO; PDB 4X9M) against the entire *M. bovis* KRB5 proteome. This file must be downloaded on your local computer for the embedded visualization scripts to function properly.
* **`pdb_models/`**: AlphaFold2 coordinate files (.pdb) for key metabolic enzymes, including:
  * **Opd (R6879_000741)**: Putative L-ascorbate-6-phosphate lactonase (UlaG homolog) featuring a TIM-barrel fold.
  * **NoxA (R6879_000281)**: Cytosolic H₂O₂-producing NADH oxidase aligned to clostridial template 6FZI.
  * **TrxB/GlpO (R6879_000062)**: FAD-dependent oxidoreductase exhibiting dual structural concordance to thioredoxin reductase and glycerol-3-phosphate oxidase.
  * **PDHc Subunits (R6879_000064–000068)**: Structural models for PdhA (E1α), PdhB (E1β), PdhC (E2 core), and PdhD (E3).

### `ptools-logs/` — Pathway Tools Execution Reports
Standardized execution logs extracted from Pathway Tools (version 29.5) providing audit trails and topological network metrics for both uncurated (`2026-08-05`) and curated (`2026-08-25`) database states:
* **`pwy-inference-report` & `pwy-rescoring-report`**: Algorithmic pathway evidence scores, taxonomic range checks, and reaction hole filling logs.
* **`dead-end-metabolites`**: Cytosolic compartment (CCO-CYTOSOL) dead-end metabolite lists detailing 37 reactant and 55 product gaps.
* **`chokepoint-reactions`**: Bipartite graph analysis cataloging 139 total cytosolic chokepoint reactions (73 producing, 66 consuming).

### `metadata/` — Cohort Epidemiological Metadata
Contains curated BioSample and demographic records for 119 closed, complete *M. bovis* RefSeq genomes with an intact *opd* locus:
* **`clean_m_bovis_119_biosamples_environmental_metadata_filled.csv`**: Master table integrating host species (*Bos taurus* vs. *Bison bison*), anatomical isolation niche (e.g. milk/mammary gland, lower respiratory tract, synovial/joint fluid), geographic country of origin, and collection era (<2010 to 2021–2023).

### `alignments_vcf/` — Population Genomics & Phylogenetics
Genomic surveillance datasets capturing evolutionary variation across the 122 closed complete genome cohort:
* **`vcf/`**: Population-wide variant calls capturing single nucleotide polymorphisms (SNPs) across the 6.6 kb L-ascorbate utilization (*ula*) operon cluster.
* **`msa/`**: Sequence Alignment/Map (SAM) format alignment files (`.sam`) capturing coding sequence alignments across the 1,029 bp *opd* gene for the 16 unique sequence genotypes identified in public databases.
* **`trees/`**: Bayesian unrooted phylogenetic tree nexus and tree files generated via MrBayes under the GTR + gamma model.

---

## 3. Database Curation Highlights & Biological Findings

Manual curation of MBVKRB5Ccyc v1.0 successfully bridged severe sequence divergence in *M. bovis*, achieving quantitative improvements across the metabolic network.

| Database Metric | Uncurated Baseline (`mbvkrb5cyc`) | Curated Database (`MBVKRB5Ccyc v1.0`) | Net Curation Impact |
| :--- | :--- | :--- | :--- |
| **Defined Pathways** | 51 | 61 | +10 pathways (+19.6%) |
| **Total Reactions** | 409 | 444 | +35 reactions (+8.6%) |
| **Enzymatic Reactions** | 371 | 393 | +22 reactions |
| **Annotated Enzymes** | 181 | 195 | +14 enzymes mapped |
| **Mapped GO Terms** | 42 | 153 | +111 terms (3.6-fold increase) |
| **Annotated Structural Features** | 0 | 79 | +79 InterPro domains/motifs |
| **Network Gap Fraction** | 27.4% (31 holes / 113 rxns) | 23.3% (30 holes / 129 rxns) | -4.1% net gap reduction |
| **Cytosolic Chokepoint Targets** | 117 | 139 | +22 drug targets (+18.8%) |

### Key Biological Findings Supported by the Repository Data

1. **Putative Alternative Carbon Shunts & Hypothesized Niche Tropism (Ascorbate & Glycerol Shunts)**:
   Manual curation identified key **putative alternative carbon shunts**—including both **putative ascorbate shunts** and **putative glycerol shunts**—that circumvent standard metabolic gaps in *M. bovis*. Structural modeling assigned a putative L-ascorbate-6-phosphate lactonase role (UlaG; TM-score 0.82) to the generic organophosphate diesterase homolog Opd (R6879_000741). This completes a putative eight-gene *ula* operon cluster (R6879_000734–R6879_000741) driving group translocation and catabolism of host L-ascorbate into lower glycolysis via a putative phosphoketolase shunt, yielding 3 ATP per molecule. Putative glycerol shunts similarly feed host-derived glycerol into central carbon metabolism and H₂O₂ redox networks.

   It is **hypothesized** that L-ascorbate import and degradation capacity is associated with anatomical niche and tissue tropism along physiological ruminant ascorbate gradients—spanning low-ascorbate rumen fluid (<1 µM), moderate plasma/synovial pools (5–40 µM), hyper-enriched milk/colostrum (57–340 µM), and dense intracellular leukocyte reservoirs (50–1,700 µM). Epidemiological surveillance links this operon to major lineage bifurcations: Clade 1 isolates strongly associate with mastitis (94.4% of milk/mammary isolates), whereas Clade 2 isolates dominate in American bison (75.0%), where host baseline plasma ascorbate levels are higher. Both shunt pathways can be directly queried in the hosted SCINet database via the [Shunt Substring Search](https://pathwaytools.scinet.usda.gov/MBVKRB5C/substring-search?type=NIL&object=shunt&quickSearch=Quick+Search).

2. **Programmed Translational Speed-Bumps in *opd***:
   Genomic surveillance across 119 closed genomes revealed 17 polymorphic wobble codons concentrated in *opd*. Synonymous substitutions in cosmopolitan Clade 2 lineages reduce the tRNA Adaptation Index (tAI sum drops from 12.99 to 10.00) and induce thermodynamic mRNA stabilization across the 200-nt target region ($\Delta\Delta G = -2.0$ kcal/mol), with local 50-nt sliding window analysis resolving a sharp thermodynamic well ($\Delta\Delta G = -6.0$ kcal/mol; local MFE shift from $-13.8$ to $-19.8$ kcal/mol) centered at midpoint 538 nt. This enforces co-translational ribosomal pauses that give the polypeptide time to fold its TIM-barrel domain under host-induced thermal and oxidative stress. Codon 186 (CAC $\rightarrow$ CAT) functions dual-role as both a speed-bump hotspot and an active-site metal-coordinating histidine.

3. **Cytosolic Redox & Peroxide Virulence Network**:
   Curation resolved H₂O₂-producing cytosolic NADH oxidase NoxA (R6879_000281; TM-score 0.97 to clostridial 6FZI) and FAD-dependent oxidoreductase TrxB (R6879_000062) with predicted moonlighting glycerol-3-phosphate oxidase (GlpO) activity. In vitro experiments confirmed that strain KRB5 generates significantly higher cytopathic H₂O₂ concentrations compared to reference strain PG45 ($P < 0.05$ at 5 minutes).

4. **Pyruvate Dehydrogenase Complex & Surface Moonlighting**:
   Manual curation assembled the four-subunit pyruvate dehydrogenase complex (PDHc; BioCyc ID CPLX2SBR-39) spanning PdhA–D (R6879_000064–R6879_000068), with 3D structural concordance (TM-scores 0.88–0.97 against PDB templates) confirming subunit identities across the complex. Cross-referencing this assembled glycolytic node with published experimental literature (Cui et al.) links the complex to a dual-function virulence role, moonlighting on the outer membrane where PdhA–D bind host fibronectin and plasminogen.

---

## 4. Web Database Access

Both the manually curated database and the automated baseline uncurated database are publicly hosted on the USDA SCINet Pathway Tools server:

* **Curated Database (MBVKRB5Ccyc v1.0)**: [https://pathwaytools.scinet.usda.gov/MBVKRB5C/organism-summary](https://pathwaytools.scinet.usda.gov/MBVKRB5C/organism-summary)
* **Uncurated Baseline Database (MBVKRB5)**: [https://pathwaytools.scinet.usda.gov/organism-summary?object=MBVKRB5](https://pathwaytools.scinet.usda.gov/organism-summary?object=MBVKRB5)
* **Carbon Shunts Quick Search (Putative Ascorbate & Glycerol Shunts)**: [https://pathwaytools.scinet.usda.gov/MBVKRB5C/substring-search?type=NIL&object=shunt&quickSearch=Quick+Search](https://pathwaytools.scinet.usda.gov/MBVKRB5C/substring-search?type=NIL&object=shunt&quickSearch=Quick+Search)
* **Host Platform**: Pathway Tools v29.5 hosted on USDA SCINet infrastructure (administered by USDA-ARS USMARC and Iowa State University).

---

## 5. License & Terms of Use

All datasets, flat-files, metadata, and structural models in this repository are dedicated to the public domain under the **Unlicense**. You are free to copy, modify, publish, use, compile, sell, or distribute this material for any purpose, commercial or non-commercial, without restriction.

---

## 6. Citation Information

If you utilize datasets, structural models, metadata, or flat-files from this research in your work, please cite the repository and the corresponding manuscripts:

### Database & Resource Report Citation
> Harhay, G. P., & Kaplan, B. (2026). Structural Curation of the MBVKRB5Ccyc Database Reveals Alternative Carbon Shunts and Redox Virulence Networks in *Mycoplasmopsis bovis*. *Microbiology Spectrum* (Under Review). Database accessible at: `https://pathwaytools.scinet.usda.gov/MBVKRB5C/organism-summary`. Data repository: `https://github.com/GregoryHarhay-USDA/MBVKRB5Ccyc`.

### L-Ascorbate Catabolism & Redox Subversion Citation
> Harhay, G. P., & Kaplan, B. (2026). Putative L-Ascorbate Catabolism and Redox Subversion of Host Leukocytes by *Mycoplasmopsis bovis*. *ASM Animal Microbiology* (Under Review). Supporting data repository: `https://github.com/GregoryHarhay-USDA/MBVKRB5Ccyc`.

### Data Repository Citation File
For automated reference management, a `CITATION.cff` file is provided in the repository root.
