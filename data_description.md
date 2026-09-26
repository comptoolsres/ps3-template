# Data Description

## File: `sequences.fasta`

### Overview

This file contains 13 partial 16S ribosomal RNA (rRNA) gene sequences from
soil microbiome samples collected at three field sites in north-central Florida.
Sequences were obtained via amplicon sequencing targeting the V3-V4 hypervariable
region of the bacterial 16S rRNA gene, using universal primers 341F / 806R.

The data in this file are **simulated for educational purposes**, based on the
structure and composition of real environmental 16S rRNA sequences deposited in
the NCBI Sequence Read Archive. They are intended to represent realistic but
fictional microbial survey data.

---

### Field Sites

| Site ID | Location              | Habitat        |
|---------|-----------------------|----------------|
| Site_A  | Paynes Prairie, FL    | Wet prairie    |
| Site_B  | Gainesville, FL       | Managed lawn   |
| Site_C  | Ocala National Forest | Longleaf pine  |

---

### Sequence Records

| Sequence ID | Site   | Sample           | Notes                                  |
|-------------|--------|------------------|----------------------------------------|
| seq_001     | Site_A | Soil_sample_1    | Clean, full-length                     |
| seq_002     | Site_A | Soil_sample_2    | Clean, full-length                     |
| seq_003     | Site_A | Soil_sample_3    | Clean, full-length                     |
| seq_004     | Site_B | Soil_sample_4    | Clean, full-length                     |
| seq_005     | Site_B | Soil_sample_5    | Clean, full-length                     |
| seq_006     | Site_B | Soil_sample_6    | Clean, full-length                     |
| seq_007     | Site_B | Soil_sample_7    | **Very short** — failed sequencing run |
| seq_008     | Site_C | Soil_sample_8    | Clean, full-length                     |
| seq_009     | Site_C | Soil_sample_9    | Clean, full-length                     |
| seq_010     | Site_C | Soil_sample_10   | Clean, full-length                     |
| seq_011     | Site_C | Soil_sample_11   | **Empty** — no sequence data recorded  |
| seq_012     | Site_C | Soil_sample_12   | Clean, full-length                     |
| seq_013     | Site_C | Soil_sample_13   | **Contains invalid characters** (X, B) |

---

### File Format

The file is in standard FASTA format:

- Each record begins with a **header line** starting with `>`
- The header contains the sequence ID, site ID, and sample ID separated by ` | `
- The nucleotide sequence follows across one or more lines
- Valid nucleotide characters are: `A`, `T`, `G`, `C`, `N`
  - `N` represents an ambiguous base (nucleotide identity uncertain)

---

### Deliberate Data Quality Issues

Three sequences have been introduced with quality issues for use in Problem 4:

| Sequence | Issue                                      |
|----------|--------------------------------------------|
| seq_007  | Sequence is only 4 bp (below 800 bp minimum) |
| seq_011  | Header present but no sequence data        |
| seq_013  | Sequence contains invalid characters `X` and `B` |

---

### Further Reading

For more information on 16S rRNA amplicon sequencing and its use in
microbial ecology, see:

- Pace, N.R. (1997). A molecular view of microbial diversity and the
  biosphere. *Science*, 276(5313), 734–740.
- The NCBI 16S rRNA database: https://www.ncbi.nlm.nih.gov/refseq/targetedloci/16S_process/
- Earth Microbiome Project: https://earthmicrobiome.org/
