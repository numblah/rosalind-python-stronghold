from lukas_data import FASTA
import re

SPLC_data = FASTA('rosalind_splc.txt')

print(SPLC_data)

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

DNA_codon = CODON_TABLE('DNA_CODON_TABLE.txt')

#make a temporary variable for the spliced DNA that will be mutated
result_string = SPLC_data.iloc[0,1]

#loop through the rest of the rows and change the value of 'result_string' with new values corresponding to what remains after substring deletions
for i in range(1,len(SPLC_data.seq)):
    result_string = result_string.replace(SPLC_data.iloc[i,1],'')

#print out for sanity
result_string

#build the protein 
protein_codons = re.findall('...', result_string)
protein = ''
for i in protein_codons:
    if DNA_codon[i] != 'Stop':
        protein +=DNA_codon[i]

#or with a list comphrehensions 
protein2 = [DNA_codon[item] for item in protein_codons if DNA_codon[item] != 'Stop' ] 
protein2 = ''.join(protein2)     
#print the protein:
        
print('here')
print('from list comprehension')
protein2
# #will need to know how many rows I have
# len(SPLC_data.seq

with open('results_file.txt', 'w') as savefile:
    savefile.write(protein2)