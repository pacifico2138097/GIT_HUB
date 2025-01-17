
''' In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.'''

# Reverse complement of a DNA string: 
def reverse_complement (input_dna):
    
    complement = {'T':'A', 'A':'T', 'C':'G', 'G':'C'}

    if not input_dna:
        return ''
    
    return complement[input_dna[-1]] + reverse_complement(input_dna[:-1])

if __name__ == "__main__":
    input_dna = 'GCAAGGCATCCACCGGCCTACCTGCGTGACTTGTTAACAAAGTATAATTGATACTACCCCATTTACAACAAGTTGATTTTGTGGGACTGGTGGGCGCTCGCTAACAATACGTATGTTCGGATCATTTGTCATAGGGTTCAGACACTTATGGCTTTTTTCCCTGCTGAACACTCGGTACTGGCGAATCAGTAAGTCCTGTCCTTCAGTACTACGGAAATTTTAGGTGGTACTACTGGGCATGAGGATCTTTTTCTAATCTACAAAGCAGTAGCGTCCCTAGACGCACCGCTATTGAAGACCGTCCATGGTGACCGTAAGAACGAATCGCGTAGAGGAGGATAACACGGTTCGACACGGGAGGCCAGCTACTTTAACATACAATTTACTGTCATAAGTCTTAAAGTGGTTATTATTTCCCCGTAACCAAAAATTCTACAACGCACAAATAGTTTATATAACACCCTACAGACTGAGGATAGAGTTGAGGTCGATGCAAGGTTGCACAGCCGGGGCAACCTAAACCTTCGTAGTTAAGGTCATTACTGATGCACGCTGGCGGGATCCTGCAAATTTGATGGAACTGTGTGAAATCGACGGGAGTAGCCAGGTCACAGACAGCCACAATTAACCGGCAGAATTTTATCGGGTGAAAGAACATCCTCGCTCACTTACCCTAGCATGGCTGGGGCAGACTTGCCAGCCGCAATGGCGTAGGTGTTCACGGTTTCGAATGTTTACACATAGCCCAGATCCACTCTTGTCTTGATCCAAGTTTCCCCAGTTGCGGAGTCAGCACCATGCCGGTGTGTGAATAGAGATAACATACGAATCAGGGGCCACATTGAGAACGAACAGAATTGGAGTCGGAGTACGTGTAGGCCCGTCGTTATACTCGGAGGGGTTGCTCCGATTTGTCTAGCCGCTCACAAAGCTCATTGTTAGC'

   
    result = reverse_complement(input_dna)

    print(result)

