
''' 
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

'''
# Function calculating the GC-content % of the string:
def gc_content(dna_sequence):
    occC = 0                     
    occG = 0
    total_length = len(dna_sequence)
    
    for char in dna_sequence:
        if char == 'C':
            occC += 1
        elif char == 'G':
            occG += 1
        
        if total_length == 0:
            return 0.0

    result = ((occC+occG)/total_length)*100   
    return result

# Converting Fasta format string into dictionary:
def parse_fasta(fasta_str):
    fasta_dict = {}
    lines = fasta_str.strip().split('\n')   
    temp_id = ""                            # temporary variable to store the ID Fasta
    temp_sequence = ""                      # temporary variable to accumulate the current sequence

    for line in lines:                   
        if line.startswith('>'):            
            if temp_id:
                fasta_dict[temp_id] = temp_sequence
            temp_id = line[1:].strip()                # updating temp_id with new ID sequence, 
            temp_sequence = ""                        # resetting temp_sequence for new record
        
        else: 
            temp_sequence += line.strip()            

    if temp_id:                                       # adding last record to the dictionary
        fasta_dict[temp_id] = temp_sequence

    return fasta_dict

# Returning highest GC-content and it's percentage:
def highest_gc_content(fasta_str):
    fasta_dict = parse_fasta(fasta_str)
    max_gc_id = None
    max_gc_content = 0.0 

    for sequence_id, dna_sequence in fasta_dict.items():
        gc_percentage = gc_content(dna_sequence)
        if gc_percentage > max_gc_content:
            max_gc_content = gc_percentage
            max_gc_id = sequence_id
    
    return max_gc_id, max_gc_content

if __name__ == "__main__":

    fasta_input = """ >Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

 """
    sequence_id, gc_content = highest_gc_content(fasta_input)
    print(f"{sequence_id}\n{gc_content:.6f}")