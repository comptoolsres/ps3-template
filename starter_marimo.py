# /// script
# requires-python = ">=3.10"
# dependencies = ["marimo"]
# ///

import marimo

__generated_with = "0.9.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # Problem Set 3: Bioinformatics with Python

        **Author:** *(your name here)*
        **Date:** *(date here)*

        This notebook works through all four problems using the file `sequences.fasta`.
        Run each cell in order from top to bottom. Read the docstrings and hints carefully
        before filling in your code.

        ---
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Setup

        Run this cell first. It sets the path to the FASTA file used throughout
        the notebook.
        """
    )
    return


@app.cell
def __():
    import marimo as mo

    # Update this path if your file is stored somewhere else
    FASTA_FILE = "sequences.fasta"

    return FASTA_FILE, mo


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ---
        ## Utility: FASTA Parser

        This function is used by all four problems — complete it before moving on.

        A FASTA file looks like this:

        ```
        >seq_001 | Site_A | Soil_sample_1
        ATGCTTACGGATCGATCG...
        TAGCTAGCTAGCGATCGA...
        >seq_002 | Site_A | Soil_sample_2
        ATGCTTACGGATCGATCG...
        ```

        Each sequence can span multiple lines. Your parser needs to assemble
        those lines into a single string per record.

        > **Marimo note:** In Marimo, cells are reactive — if you change
        > `parse_fasta`, all cells that call it will automatically re-run.
        """
    )
    return


@app.cell
def __(FASTA_FILE):
    def parse_fasta(filepath):
        """
        Reads a FASTA file and returns a list of (header, sequence) tuples.

        Parameters
        ----------
        filepath : str
            Path to the FASTA file.

        Returns
        -------
        list of tuple
            A list of (header, sequence) tuples, e.g.:
            [("seq_001 | Site_A | Soil_sample_1", "ATGC..."), ...]

        Hints
        -----
        - Use a for loop to read the file line by line.
        - Use an if statement to check whether a line starts with '>'.
        - You will need variables to keep track of the current header
          and the sequence being assembled across multiple lines.
        - What should you do when you encounter a new header while
          you already have a sequence stored?
        """

        records = []

        # --- Your code here ---

        return records


    # Test your parser — this previews headers and the first 40 characters
    # of each sequence so you can verify it's working.
    records = parse_fasta(FASTA_FILE)

    for header, seq in records:
        print(f"{header} : {seq[:40]}...")

    return parse_fasta, records


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ---
        ## Problem 1: Sequence Lengths (5 pts)

        Print the header and length of each sequence.

        **Expected output format:**
        ```
        seq_001 | Site_A | Soil_sample_1 : 1247 bp
        seq_002 | Site_A | Soil_sample_2 : 1193 bp
        ...
        ```
        """
    )
    return


@app.cell
def __(records):
    def print_sequence_lengths(records):
        """
        Prints the header and length of each sequence.

        Parameters
        ----------
        records : list of tuple
            A list of (header, sequence) tuples as returned by parse_fasta().
        """

        # --- Your code here ---

        pass


    print_sequence_lengths(records)
    return (print_sequence_lengths,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ---
        ## Problem 2: GC Content (5 pts)

        Calculate and report GC content statistics across all sequences.

        GC content is the fraction of bases that are G or C:

        $$\text{GC}\% = \frac{\text{count}(G) + \text{count}(C)}{\text{total length}} \times 100$$

        You must write a `calculate_gc(sequence)` function and call it
        from `report_gc_stats()`.
        """
    )
    return


@app.cell
def __():
    def calculate_gc(sequence):
        """
        Calculates the GC content of a nucleotide sequence as a percentage.

        Parameters
        ----------
        sequence : str
            A nucleotide sequence string.

        Returns
        -------
        float
            GC content as a percentage (0.0 to 100.0).

        Hints
        -----
        - str.count() counts occurrences of a character.
        - Think about what to return if the sequence is empty.
        """

        # --- Your code here ---

        pass

    return (calculate_gc,)


@app.cell
def __(calculate_gc, records):
    def report_gc_stats(records):
        """
        Prints GC content for each sequence and reports the highest,
        lowest, and average GC content across all sequences.

        Parameters
        ----------
        records : list of tuple
            A list of (header, sequence) tuples as returned by parse_fasta().

        Hints
        -----
        - Call calculate_gc() for each sequence.
        - Keep track of the highest and lowest values as you iterate.
        """

        # --- Your code here ---

        pass


    report_gc_stats(records)
    return (report_gc_stats,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ---
        ## Problem 3: Motif Search (5 pts)

        Search each sequence for the *Eco*RI restriction site `GAATTC` and report:
        - The count per sequence
        - Which sequence has the most occurrences
        - The total count across all sequences

        **Bonus (+2 pts):** Use Marimo's UI to make the motif interactive —
        see the hint cell below.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        > **Marimo bonus hint:** Marimo has built-in UI elements. You could make
        > the motif input interactive like this:
        >
        > ```python
        > motif_input = mo.ui.text(value="GAATTC", label="Search motif:")
        > motif_input
        > ```
        >
        > Then use `motif_input.value` wherever you need the motif string.
        > Any cell that depends on `motif_input.value` will automatically
        > re-run when you change the input — no need for a button!
        """
    )
    return


@app.cell
def __():
    def count_motif(sequence, motif):
        """
        Counts non-overlapping occurrences of a motif in a sequence.

        Parameters
        ----------
        sequence : str
            A nucleotide sequence string.
        motif : str
            The motif to search for (e.g., "GAATTC").

        Returns
        -------
        int
            Number of non-overlapping occurrences.

        Hints
        -----
        - Python strings have a built-in method that does exactly this.
        - Make the search case-insensitive.
        """

        # --- Your code here ---

        pass

    return (count_motif,)


@app.cell
def __(count_motif, records):
    def report_motif_stats(records, motif="GAATTC"):
        """
        Searches for a motif in each sequence and prints a summary.

        Parameters
        ----------
        records : list of tuple
            A list of (header, sequence) tuples as returned by parse_fasta().
        motif : str, optional
            The motif to search for. Defaults to "GAATTC" (EcoRI site).
        """

        # --- Your code here ---

        pass


    report_motif_stats(records, motif="GAATTC")
    return (report_motif_stats,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ---
        ## Problem 4: Quality Control (5 pts)

        Check each sequence for quality issues and print `[PASS]` or `[WARN]`.

        Warn if:
        - The sequence contains characters other than `A`, `T`, `G`, `C`, or `N`
        - The sequence is shorter than **800 bp**
        - The sequence is longer than **1600 bp**
        - The sequence record has no data at all

        **Expected output format:**
        ```
        [PASS] seq_001 | Site_A | Soil_sample_1
        [WARN] seq_007 | Site_B | Soil_sample_7 — sequence too short (4 bp)
        [WARN] seq_011 | Site_C | Soil_sample_11 — no sequence data
        [WARN] seq_013 | Site_C | Soil_sample_13 — invalid characters detected
        ```
        """
    )
    return


@app.cell
def __(records):
    def qc_check(records):
        """
        Quality control checker. Prints [PASS] or [WARN] for each sequence.

        Parameters
        ----------
        records : list of tuple
            A list of (header, sequence) tuples as returned by parse_fasta().

        Hints
        -----
        - Use a set of valid characters for fast membership checking.
        - A sequence with no data will be an empty string.
        - A single sequence can trigger more than one warning.
        """

        valid_bases = set("ATGCN")

        # --- Your code here ---

        pass


    qc_check(records)
    return (qc_check,)


if __name__ == "__main__":
    app.run()