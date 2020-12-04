from lukas_data import FASTA
import re
from time import time
start_time = time()
SPLC_data = FASTA('rosalind_lcsm.txt')

print(SPLC_data)
# clean function rewrite

def find_unique_motifs(string):
    """pass a string to find motifs in"""
    listing_motifs = []
    #loop through the string to find all starting positions of a string
    for i in range(len(string)+1):
        #loop to find all end positions of a string
        for n in range(len(string)+1):
            #only count when the start position is before the end position
            #avoids empty strings
            if i < n:
                #append the string
                listing_motifs.append(string[i:n])
    #return a sorted (longest to shorts) list of unique motifs            
    return sorted(set(listing_motifs), key=len, reverse=True)

def find_common_motif_in_list(series, motifs_to_check):
    """takes a series of sequences and a list of motifs to find which motif is the most common"""
    # confirm that the list is sorted and unique
    sorted(set(motifs_to_check), key=len, reverse=True)
    #for every motif
    for n in motifs_to_check:
        #start counting
        counter = 0 
        
        # for every member in a series
        for i in range(len(list(series))):
            #check if motif is in one member at least, 
            if n in series[2]:
            #if a motif is in that member
                if n in series[i]:
                #add to the counter
                    counter += 1
                #if at any point the motif is not found in series, the loop is broken immediatelly     
                else:
                    break    
            else:
                #if not another motif will be tested
                break

        #if the counter is the same as the length of the series
        # meaning that the motif was found in each of the strings
        # return that motif and break the loop        
        if counter == len(list(series)):
            return n
            break
        # else keep going, the loop now goes to the next motif
        # this could be adapted to find all common motifs not just the longest one
        # simply removing the break above  
        else:
            continue
    
motifs = find_unique_motifs(SPLC_data.iloc[0,1])
answer = find_common_motif_in_list (SPLC_data.seq, motifs)
print('answer', answer)

end_time = time() - start_time
print('Time passed:', end_time)

with open('LCSM_results.txt', 'w') as file:
    file.write(answer)

#used this code to find how many test loops are needed
# print('Start the optimisation process:')
# for timo in [2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
#     start_time = time()
#     print('Time#######:', timo)
#     print(find_common_motif_in_list (SPLC_data.seq, motifs, timo))
#     print(time()-start_time)
    



# print('answer', answer)

# with open('LCSM_results.txt', 'w') as file:
#     file.write(answer)


# belows is the 'working' process


#doesn't matter that there are different length strings given
#if I have the longest (as first in input) one I will find what matches the shortest string
#IF I get the shortest the most common motif can't be longer than that

# list_of_motifs = []
# for i in range(len(SPLC_data.iloc[0,1])+1):
#     for n in range(len(SPLC_data.iloc[0,1])+1):
#         if i < n :    
#             list_of_motifs.append(SPLC_data.iloc[0,1][i:n])

# unique_motif_list = sorted(set(list_of_motifs), key=len, reverse=True)

# loop through all strings and check if motif is present in all items
#if not continue to the next motif
#if yes print the motif 
#if there are competing common motifs it will give the first one in the motif lsit

# list(SPLC_data.seq)


# print ('answer:')
# for n in unique_motif_list:
#     counter = 0
#     for i in range(len(list(SPLC_data.seq))):
#         if n in SPLC_data.seq[i]:
#             counter += 1
#     if counter == len(list(SPLC_data.seq)):
#         print(n)
#         break
#     else:
#         continue      


# for i in range(len(list(SPLC_data.seq))):
#     counter = 0
#     for n in unique_motif_list:
#         if n in SPLC_data.seq[i]:
#             counter += 1
#         if counter == len(list(SPLC_data.seq)):
#             print()       
