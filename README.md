# Problem Set 3: Bioinformatics with Python

In completing this, you can use Python scripts or Marimo or Jupyter Notebooks.

You may work on this in groups or on your own. If you work as a group, you should create the group in Canvas so that you are not assigned to review another submission from your group.

Even if you work in groups, **each person must submit the assignment in Canvas** for the peer review process to work.

**Note:** This assignment will have peer review. It is important to be able to look at someone else's code and figure out what they are doing. It's also important to write code with the idea that someone else will look at it and needs to understand it. While I will take both the peer reviewer's comments on your code and your comments on the peer reviewed code into account when assigning grades, I will be assigning the grade, not the reviewer.

---
## Starter code

There are three versions of the starter code depending on how you wish to work:

1. `starter_script.py` A pure Python script. Generally run from the command-line.
2. `started_jupyter.ipynb` A Jupyter Notebook with instrcutions in markdown format and code blocks with starter code.
3. `starter_marimo.py` A Marimo Notebook with instrcutions in markdown format and code blocks with starter code.
    * Before launching Marimo, you will need to clone the repo onto HiPerGator, change directories into the problem set directory, and run:
        ```bash
        ml conda
        uv init
        ```

---

## Data

The data file for this problem set is:
`sequences.fasta`

It is included in this repository. See `data_description.md` for full metadata.

---

## Background

The file `sequences.fasta` contains 16S ribosomal RNA (rRNA) gene sequences from soil microbiome samples collected at three sites in north-central Florida. The 16S rRNA gene is a highly conserved region of bacterial and archaeal genomes that is widely used in environmental microbiology to identify and classify microorganisms without culturing them. Each sequence in the file represents a unique bacterial isolate or environmental sequence variant (amplicon sequence variant, ASV).

Understanding the composition of these sequences, their lengths, GC content, and the presence of specific motifs, is a first step in characterizing microbial communities.

---

## File Format: FASTA

A FASTA file is a plain text format for nucleotide or protein sequences. Each record has two parts:

1. A **header line** beginning with `>`, containing the sequence ID and optional description
2. One or more lines of **sequence data**

Example:

    seq_001 | Site_A | Soil_sample_1
    ATGCTTACGGATCGATCGATCGATCGATCGGCTAGCTAGCTAGCTAGCTAGC
    TAGCTAGCTAGCGATCGATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAG


Your scripts will need to handle the fact that a single sequence may span multiple lines.

---

## Problems

### Problem 1 (5 pts)

Opens `sequences.fasta` and use a `for` loop to read through the file line by line, and print the **sequence ID** and **length** (in base pairs) of each sequence in the file after reading is complete.

**Hint:** You will need to keep track of which sequence you are currently reading. What happens when you encounter a new `>` header line while already building a sequence?

**Expected output format:**

    seq_001 | Site_A | Soil_sample_1 : 1247 bp
    seq_002 | Site_A | Soil_sample_2 : 1193 bp
    ...


---

### Problem 2 (5 pts)

Calculate the **GC content** of each sequence and report:

- The sequence with the **highest** GC content (ID and percentage)
- The sequence with the **lowest** GC content (ID and percentage)
- The **average** GC content across all sequences

GC content is calculated as:

    GC content (%) = (count of G + count of C) / total length × 100


Write a **function** called `calculate_gc(sequence)` that takes a sequence string and returns the GC content as a percentage.

---

### Problem 3 (5 pts)

Search each sequence for the motif `GAATTC` (the recognition site for the restriction enzyme *Eco*RI). Your script should:

- Count how many times the motif appears in each sequence
- Report the sequence ID with the **most occurrences** and its count
- Report the **total number** of motif occurrences across all sequences

Write a **function** called `count_motif(sequence, motif)` that takes a sequence string and a motif string, and returns the count of non-overlapping occurrences.

**Bonus (+2 pts):** Modify your function so that the motif to search for can be supplied as a command-line argument, so the same script can be reused for any motif.

---

### Problem 4 (5 pts)

Imagine the FASTA file is being written in real time as sequences come off a sequencer. Write a script (or Jupyter Notebook) that acts as a quality control checker: as each sequence is fully read in, print a **warning** if any of the following occur:

- The sequence contains characters other than `A`, `T`, `G`, `C`, or `N`
- The sequence is shorter than **800 bp**
- The sequence is longer than **1600 bp**
- A header line appears immediately followed by another header line (i.e., a sequence with no data)

For sequences that pass all checks, print a confirmation:


    [PASS] seq_001 | Site_A | Soil_sample_1
    [WARN] seq_007 | Site_B | Soil_sample_3 - sequence too short (312 bp)
    [WARN] seq_015 | Site_C | Soil_sample_9 - invalid characters detected

---

## Grading

| Problem | Points |
|---------|--------|
| Problem 1 | 5 |
| Problem 2 | 5 |
| Problem 3 | 5 |
| Problem 4 | 5 |
| Bonus | +2 |
| **Total** | **20 (+2)** |

Grades will reflect both correctness and code readability. Use comments, meaningful variable names, and docstrings in your functions.