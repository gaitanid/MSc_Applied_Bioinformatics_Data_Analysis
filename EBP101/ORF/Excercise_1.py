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

def process_bacterial_sequences():
    # Process bacterial DNA sequences until the user types 'exit'
    while True:
        print("Type a DNA sequence (or type 'end' to end):")
        dna_sequence = input().upper()

        if dna_sequence.lower() == 'end':
            break

        # Check if the DNA sequence contains only valid nucleotides
        for nucleotide in dna_sequence:
            if not is_valid_nucleotide(nucleotide):
                print(f"Invalid sequence: {nucleotide}. Use only A, T, G, C or a, t, g, c.")
                break
        else:
            # If the sequence is valid, find and print the protein sequence
            find_protein_sequence(dna_sequence)

if __name__ == "__main__":
    process_bacterial_sequences()

