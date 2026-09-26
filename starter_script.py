# =============================================================================
# Problem Set 3: Bioinformatics with Python
# Starter Script
#
# This file provides the function signatures and structure for all four
# problems. You are encouraged to use this as a starting point, but you
# are not required to. You may also complete the problems in separate scripts
# or Jupyter Notebooks.
#
# Author: [Your name here]
# Date:   [Date here]
# =============================================================================

# The path to the FASTA file. Update this if your file is in a different location.
FASTA_FILE = "sequences.fasta"


# =============================================================================
# Utility: FASTA Parser
# =============================================================================

def parse_fasta(filepath):
    """
    Reads a FASTA file and returns a list of (header, sequence) tuples.

    Each element of the list represents one sequence record. The header
    is the full text of the '>' line (without the '>'), and the sequence
    is the complete nucleotide string assembled from all sequence lines
    belonging to that record.

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
    - You will need variables to keep track of the current header and
      the sequence being assembled across multiple lines.
    - What should you do when you encounter a new header and you already
      have a sequence stored?
    """

    records = []

    # --- Your code here ---

    return records


# =============================================================================
# Problem 1: Sequence lengths
# =============================================================================

def print_sequence_lengths(records):
    """
    Prints the header and length of each sequence in the records list.

    Parameters
    ----------
    records : list of tuple
        A list of (header, sequence) tuples as returned by parse_fasta().

    Expected output format
    ----------------------
    seq_001 | Site_A | Soil_sample_1 : 1247 bp
    seq_002 | Site_A | Soil_sample_2 : 1193 bp
    ...
    """

    # --- Your code here ---

    pass


# =============================================================================
# Problem 2: GC content
# =============================================================================

def calculate_gc(sequence):
    """
    Calculates the GC content of a nucleotide sequence.

    GC content is the percentage of bases that are either G or C:
        GC (%) = (count of G + count of C) / total length * 100

    Parameters
    ----------
    sequence : str
        A nucleotide sequence string (e.g., "ATGCTAGC...").

    Returns
    -------
    float
        The GC content as a percentage (0.0 to 100.0).

    Hints
    -----
    - You can use str.count() to count occurrences of a character.
    - Think about what to return if the sequence is empty.
    """

    # --- Your code here ---

    pass


def report_gc_stats(records):
    """
    Calculates and prints GC content statistics across all sequences.

    Prints:
    - The GC content of each sequence
    - The sequence with the highest GC content
    - The sequence with the lowest GC content
    - The average GC content across all sequences

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


# =============================================================================
# Problem 3: Motif searching
# =============================================================================

def count_motif(sequence, motif):
    """
    Counts the number of non-overlapping occurrences of a motif in a sequence.

    Parameters
    ----------
    sequence : str
        A nucleotide sequence string.
    motif : str
        The motif to search for (e.g., "GAATTC").

    Returns
    -------
    int
        The number of times the motif appears in the sequence.

    Hints
    -----
    - Python strings have a built-in method that counts non-overlapping
      occurrences. Can you find it?
    - Make sure your search is case-insensitive, or convert both strings
      to the same case before searching.
    """

    # --- Your code here ---

    pass


def report_motif_stats(records, motif="GAATTC"):
    """
    Searches each sequence for a motif and reports summary statistics.

    Prints:
    - The motif count for each sequence
    - The sequence with the most occurrences of the motif
    - The total number of occurrences across all sequences

    Parameters
    ----------
    records : list of tuple
        A list of (header, sequence) tuples as returned by parse_fasta().
    motif : str, optional
        The motif to search for. Defaults to "GAATTC" (EcoRI site).
    """

    # --- Your code here ---

    pass


# =============================================================================
# Problem 4: Quality control checker
# =============================================================================

def qc_check(records):
    """
    Performs a quality control check on each sequence and prints the result.

    For each sequence, prints either:
        [PASS] <header>
    or one or more warning lines:
        [WARN] <header> — <reason>

    Warnings are triggered by:
    - Invalid characters (anything other than A, T, G, C, or N)
    - Sequence shorter than 800 bp
    - Sequence longer than 1600 bp
    - A sequence record that has no sequence data (empty string)

    Parameters
    ----------
    records : list of tuple
        A list of (header, sequence) tuples as returned by parse_fasta().

    Hints
    -----
    - Use a set of valid characters for efficient membership checking.
    - For detecting invalid characters, consider iterating over the
      sequence and checking each base, or using a set comparison.
    - A sequence record with no data will have an empty string as its
      sequence — this is how parse_fasta() should represent it.
    """

    valid_bases = set("ATGCN")

    # --- Your code here ---

    pass


# =============================================================================
# Main: Run all problems
# =============================================================================

if __name__ == "__main__":

    # Parse the FASTA file
    records = parse_fasta(FASTA_FILE)

    # Problem 1
    print("=" * 60)
    print("PROBLEM 1: Sequence Lengths")
    print("=" * 60)
    print_sequence_lengths(records)

    # Problem 2
    print("\n" + "=" * 60)
    print("PROBLEM 2: GC Content")
    print("=" * 60)
    report_gc_stats(records)

    # Problem 3
    print("\n" + "=" * 60)
    print("PROBLEM 3: Motif Search (EcoRI: GAATTC)")
    print("=" * 60)
    report_motif_stats(records, motif="GAATTC")

    # Problem 4
    print("\n" + "=" * 60)
    print("PROBLEM 4: Quality Control")
    print("=" * 60)
    qc_check(records)