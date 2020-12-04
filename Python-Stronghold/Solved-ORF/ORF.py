from lukas_data import FASTA
import re
# from lukas_data import CODON_TABLE

# with open('sample_input.txt', 'r') as f:
#     data = f.read()
#get the data in
data_parsed = FASTA('rosalind_orf.txt')
test_string = str(data_parsed.seq[0])

def CODON_TABLE(filename):
        #read in the codon table
    with open(filename, 'r') as file:
        data = file.read()
    data.split()
    #scans the data and returns two lists one for codons the other for matching amino acids
    list_of_codons = [item for item in data.split() if len(item) == 3]
    list_of_amino_acids = [item for item in data.split() if len(item) != 3]
    DNA_codon_dict = {}
    #making a codon:amino_acid dictionary avoids this problem
    items2 = zip(list_of_codons, list_of_amino_acids)
    #create two variants of of ziped lists
    return {key:value for (key,value) in items2}

def rev_complement (string_name):
    # users  input is read here
    # make a reverese complement dictionary
    complement={'A':'T','T':'A','G':'C','C':'G'}
    #reverse the sequence (could have done in the the list comprehension)
    data_rev=string_name[::-1]
    #create a new string by looping through the reverse string and
    #picking the corresponding base using the disctionary
    return ''.join([complement[base] for base in data_rev])
    #lastly, make a new file and save the output
# print(DNA_codon_dict)

codon_table = CODON_TABLE('DNA_CODON_TABLE.txt')
#FINAL version
def orf_finder_robust2(DNA_string):
    list_of_proteins = []
    complement={'A':'T','T':'A','G':'C','C':'G'}
    data_rev=DNA_string[::-1]
    rev_string = ''.join([complement[base] for base in data_rev])
    both_strings = [DNA_string, rev_string]
    for DNA_strand in both_strings:
        for i in range(3): # because three reading frames can exist
            codon_list = re.findall('...',DNA_strand[i:])
            for number, codon in enumerate(codon_list):
                if codon == 'ATG': #is this the first instance of detecting 'ATG'?
                    protein = '' #prepare an empty protein variable
                    #make a loop to build a protein starting from the codon number corresponding to the first detected ATG
                    for codon_2 in codon_list[number:]:
                        #is the codon 'Stop'?
                        if codon_table[codon_2] == 'Stop':
                            #if so add stop to the end. This labels the protein string as a real ORF as it ends with 'Stop'
                            protein += codon_table[codon_2]
                            #and break the loop to terminate the process
                            break
                        if len(codon_2) == 3: # otherwise add to protein the amino acid if codon if fine (this is in case there are aberrant codons at tail ends for some reason)
                            protein += codon_table[codon_2]
                    if protein.endswith('Stop'): # filter all output for ORFs
                        #remove 'Stop' from ORFS and add to the list
                        list_of_proteins.append(protein.rstrip('Stop'))        
    #only onclude unique values and convert them back into a list
    return list(set(list_of_proteins))

print('check function:')
print('\n')
for i in orf_finder_robust2(test_string):
    print(i)
print('\n')
print('results saved into a file')


with open('result.txt', 'w') as the_file:
    for i in orf_finder_robust2(test_string):
        the_file.write(i+'\n')  







#################################################
#################################################
#################################################
#################################################
#orf_finder did not work for rosalind because it: identifies all ORFs within a string and it identifies M within another ORF as an another ORF
def orf_finder(list_with_both_strings):
    #make an emty list to fit the answer
    list_of_orf = []
    # loop through the main and reverse strands always two items
    for i in list_with_both_strings:
        #find ATG codon locations
        locations = [item.start() for item in re.finditer('ATG', i)]
        #loop through atg locations 
        for n in locations:
            #define an empty protein 
            protein = ''
            #split the sequence starting at one of the locations into sets of three
            protein_codon_list = re.findall('...',i[n:])
            #loop to build a protein
            for y in protein_codon_list:
                if codon_table[y] == 'Stop':
                    break
                elif len(y) == 3:
                    protein += codon_table[y]
            
            list_of_orf.append(protein)
    return list_of_orf    


#################################################
#################################################
#################################################
#################################################
# orf_finder(both_strings)

#not so robust, as an ORF finder it leaves in sequences that get terminated 'unnaturally'
def orf_finder_robust(DNA_string):
    list_of_proteins = []
    complement={'A':'T','T':'A','G':'C','C':'G'}
    data_rev=DNA_string[::-1]
    rev_string = ''.join([complement[base] for base in data_rev])
    both_strings = [DNA_string, rev_string]
    for DNA_strand in both_strings:
        for i in range(3): # because three reading frames can exist
            codon_list = re.findall('...',DNA_strand[i:])
            count=0 # count how many times I've detected 'ATG' for the current time I only am looking for one
            for number, codon in enumerate(codon_list):
                if codon == 'ATG' and count == 0: #is this the first instance of detecting 'ATG'?
                    count += 1 #notify the count number that 'ATG' has been detected
                    protein = '' #prepare an empty protein variable
                    #make a loop to build a protein starting from the codon number corresponding to the first detected ATG
                    for codon_2 in codon_list[number:]:
                        if codon_table[codon_2] == 'Stop': # if there is a stop codon detected, break the loop
                            break
                        elif len(codon_2) == 3: # otherwise add to protein the amino acid if codon if fine (this is in case there are aberrant codons at tail ends for some reason)
                            protein += codon_table[codon_2]
                    list_of_proteins.append(protein)        
    return list(set(list_of_proteins))
