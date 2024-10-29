
''' A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s
 of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.'''

# Function counting the nucleotides in the string:
def countNucleotides(input_dna):
    
    result = []

    occA = 0    # initializing counts = 0 
    occT = 0
    occC = 0
    occG = 0

    for i in input_dna:    # if A is in the string increment the occA by 1, same for the other characters.
        if i == 'A':
            occA += 1
        elif i == 'C':
            occC += 1
        elif i == 'G':
            occG += 1
        elif i == 'T':
            occT += 1

    result.append(occA)   # adding each nucleotide count to the result list
    result.append(occC)
    result.append(occG)
    result.append(occT)

    return result
 
if __name__ == '__main__':
     input_dna= 'ACCGATGAGGACACAACTATATTTGTCTTCGGCGACCCGTCTATATAGTCAGTGGGTTTAGAAATAGGGTATCCGGTGAACTGACAGCTTCTAGCGACGGGCCGCCCAATAGCTGAGAAGGACCTTGTCATAGGTGGTGGGAATGAGTTGAGCGTCGGCCGATGTACGGCCTTCTGTGACGCAGAAGAGCATGCGCTCACGGCAGGGGGGAGTGTCTAGTATTGCGGTTTGTAAGTTACTAGCCTAACCTATCTTGGGTGCGACCGGAGTCATCTATGTACGTGCCATTAAAAGGGGTGCTACACGTGGCGGGTTTTGCAGGAGGTGCCCTGCCGCGGCATGCCAAGAATTAGTAAGTGCAGAGAATCTGTGCCACCGTGTGTCTAGATTAGACATTCATCAACGCGGCTAGTTAAGATCATAGCCCAAACCCGAACGCCGAAGCATCACCTCCTGAGACCAAGGCCGTCCCAAAGATTCGCACAAATTTCACTAAATCCGGGACGTCGCATAGGTGGTACCAGATGGGCCGGGATGCCAGTGATTACCTCAGCGTGTCCCTCTCCCTTATAGGCACTCAGGCCAATTCGGTTTGCCTGAAATGGAACGGACTGCCTGGCAATACTGGCTTTTTTGATCTCATCTTGCGGATTAACGTTCTGGAGTCTTCAAGGCTTAACGACAAGTACTCACTCGATACCACAGCCGTATTTAGGCCATAGGTTCTGTCTGCCACATTGAAACACCCGCCTACGTGTTTGCCAAAATGATCCTTGCATGGTCCAGCGCTGATGCAATGGCTAGGAGAAATGGATCGAGTGTTAATCGCTTGTGGATTGCTCTAGACATCCGTTTTTATGCCTCCGTGTTGCATACAAATGCTAACCTTA'
    
     result = countNucleotides(input_dna)
    
     print(*result)