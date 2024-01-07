import re
from Bio import SeqIO

def read_sequence_file(filepath):
    # Read a sequence from a file using Biopython's SeqIO
    with open(filepath, 'r') as file:
        for seq_record in SeqIO.parse(file, "fasta"):
            return str(seq_record.seq)

def is_valid_nucleotide(nucleotide):
    # Check if the nucleotide is valid (A, T, G, C in both upper and lower case)
    valid_nucleotides = set("ATGCatgc")
    return nucleotide in valid_nucleotides

def find_start_codon(sequence):
    # Find the position of the start codon (ATG) in the given DNA sequence
    start_codon = "ATG"
    sequence_upper = sequence.upper()  # Convert to uppercase for case-insensitive search
    return sequence_upper.find(start_codon)

def find_stop_codon(sequence, start_position):
    # Find the position of the stop codon (TAA, TAG, TGA) after the given start position
    stop_codons = ["TAA", "TAG", "TGA"]
    for i in range(start_position, len(sequence), 3):
        codon = sequence[i:i + 3].upper()
        if codon in stop_codons:
            return i
    return -1

def find_protein_sequence(sequence):
    # Find the start position of the start codon
    start_pos = find_start_codon(sequence)

    if start_pos == -1:
        print("No start codon (ATG) found.")
        return

    # Find the position of the stop codon after the start codon
    stop_pos = find_stop_codon(sequence, start_pos)

    if stop_pos == -1:
        print("No stop codon found.")
        return

    # Extract and print the protein sequence between the start and stop codons
    protein_sequence = sequence[start_pos:stop_pos + 3]
    print(f"The ORF is: {protein_sequence}")

def complementary_ORF_finder(sequence):
    # Find ORFs in the complementary sequence
    start_codon = "ATG"
    start_positions = [match.start() for match in re.finditer(start_codon, sequence)]

    orfs = []  # to store the found ORFs

    for start_pos in start_positions:
        stop_pos = find_stop_codon(sequence, start_pos)
        if stop_pos != -1:
            orf_sequence = sequence[start_pos:stop_pos + 3]
            orfs.append(orf_sequence)

    return orfs

def process_sequence(sequence):
    # Check if the DNA sequence contains only valid nucleotides
    if all(is_valid_nucleotide(nucleotide) for nucleotide in sequence):
        # If the sequence is valid, find and print the protein sequence
        find_protein_sequence(sequence)
        # Also find ORFs in the complementary sequence
        complementary_orfs = complementary_ORF_finder(sequence)
        
        # Display all complementary ORFs found
        if complementary_orfs:
            print("ORFs:")
            for orf in complementary_orfs:
                print(orf)
    else:
        print("Invalid sequence. Use only A, T, G, C or a, t, g, c.")

def main():
    while True:
        user_input = input("\nThis is an ORF-detecting program for DNA sequences.\n"
                           "Type 'file' to read sequence from a file or enter your sequence directly.\n"
                           "Type 'exit' to end the program.\n"
                           "Your choice: ")

        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break

        if user_input.lower() == 'file':
            filepath = input("Enter the file path: ")
            sequence = read_sequence_file(filepath)
        else:
            sequence = user_input

        if "U" in sequence:
            print("Your sequence is an RNA sequence NOT a DNA sequence. I am sorry for this.\n")
            continue

        print("Proceeding with ORF finding.\n")
        process_sequence(sequence)

if __name__ == "__main__":
    main()
