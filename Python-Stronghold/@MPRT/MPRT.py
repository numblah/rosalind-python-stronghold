import requests
from lukas_data import FASTA
import re

#load in uniprot ids as a list - function
def load_in_uniprot_id(file_name):
    with open(file_name, 'r') as file:
        return [item.rstrip('\n') for item in file.readlines()]
#loop through a list and download all into single file - funciton

def uniprot_download_to_multi_fasta(uniprot_id_list, file_name_string):
    #make a string to store all fasta files first
    all_fasta = ''
    for uni_id in uniprot_id_list:
        url = 'https://www.uniprot.org/uniprot/'+str(uni_id)+'.fasta'
        
        all_fasta += requests.get(url).text
    with open(file_name_string, 'w') as file_fasta:
        file_fasta.write(all_fasta)

# use FASTA function and open the file
    #already written
#add UniprotID column to the data frame from FASTA

def find_regex_locations_in_string(string,regex='(?=(N[^P][ST][^P]))'):
    return ' '.join([str(item.start()+1) for item in re.finditer(regex, string)])
    

#loop through seq column - function 
#detect instances and find locations of the pattern (N{P}[ST]{P}) using regex
    #use the lookahead regex 
[item.start()+1 for item in re.finditer('(?=(N[^P][ST][^P]))', 'OIJJHNSTNMMNPSSPNNJTJN')]

#print ID and the locations

#execturion
#get list of uniprot IDs from a txt file
uniprot = load_in_uniprot_id('rosalind_mprt.txt')
#use the list to download sequences and put together a fasta file
uniprot_download_to_multi_fasta(uniprot, 'just_tryn.fasta')
#use my FASTA parser to obtain a data frame
uniprot_df = FASTA('just_tryn.fasta')
#add handy uniprot labels to the data frame from the original uniprot id list
uniprot_df['ID_uniprot'] = uniprot


#open a results file with 'w' to clear any contents added before (will be using append)
with open('MPRT_results', 'w') as file:
    file.write('')

#make a loop to go throuh the sequences in the data frame and apply the pattern matching function

for i in range(len(uniprot_df.seq)):
    #filter only for those sequences that return non zero length lists as results
        #meaning only those that matched something
    if len(find_regex_locations_in_string(uniprot_df.iloc[i,1])) >0:
        #sanity check printing
        print(uniprot_df.iloc[i,2])
        print(find_regex_locations_in_string(uniprot_df.iloc[i,1]))
        #open results file and append the information
        with open('MPRT_results', 'a') as file:
            file.write(uniprot_df.iloc[i,2])
            file.write('\n')
            file.write(find_regex_locations_in_string(uniprot_df.iloc[i,1]))
            file.write('\n')
