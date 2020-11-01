import sys
import pandas as pd
# import numpy as np
#outstnading fixes:
#need to fix the fasta import
#dictionary/sorted output does not save for some reason

def FASTA(data):
    import pandas as pd
    
    split_data=data.split('>')

    del split_data[0]
    split_data

    for index, element in enumerate(split_data):
        split_data[index]=element.split('\n',1)

    data_df=pd.DataFrame (split_data, columns=['ID','seq']) 
    data_df['seq'].replace(regex=True, inplace=True, to_replace='\n', value=r'')
    return(data_df)

# input_data = [line.rstrip() for line in open(sys.argv[1])] keep for deployment

input_data = [line for line in open('rosalind_revp.txt')]
#need to select [0] as it is a string within a list

#at this step If I had multifasta I could loop through and store FASTA IDs in on list and corresponding sequences in another by filtering through a condition 'if '>' in item'
input_data_2 = ''.join(input_data)

input_data_2 = FASTA(input_data_2)

input_data_2 = input_data_2['seq'][0]
# input_data_2 ='CGCGGATCAGGGCACTGTAGGGTGCTGTTACAGCGAATACCACACGAACTTCAAGGTTCTTCCCAGGGCGTCCAGAGTCTATTTAAGGTTTAACATTTGGAGTAGCGGAGTTGTTGTTTTAGGCGACTCAAGATCCAGCGGTAACCCTGTGCAAATTAGTCTCGGGGTGTGCACAGCCGTTCAGCCCCTGGTCACATCCGCACCGAGATGTTGCTTGGGGCTTGGGTGTCATGCTGACGCAAGGAGTGGCGCGGTCTTTCTCCCGTTCCGCATGACTGTGCTCAGACTGACCTGGGTCGTATTTGACATTGCGAATGCTAATCGATGGAGTTTAGCGAGCCCATTTAAATTGAATCCTATCCTGGTACAGGGTCTTGTTCTGTCAGAGTCGCGGAGGACGGATGCGAGCATAGTATCTCACCCTCACATGATCATGTTCCCAATGCTCAAAGTTAGAGGGGCGACGACTGCACGTATCAAGCAGACACTGGCATCTAGACGGTACCGTAGCTTGAACGTAGCCACCGAGATTCAATAGAGTGTGAGACTACGTGATATATGTTGCACTTGTAGTCGTTGGCTACCAAGAGTGCAACTGTATCTGATCCTACCTCCTAGTACGGGTTCCCGCGGCTACTTGCTGTGTTTAGGAGTCTGGGGGGTTGTGCTTTCCCTCAGATTAGAAGGACACCCCTGTGATTGGCATTAGCGGGCAGTGGAAGTACCCCCCCGTACTTAGTTATCCGTGTCGTCTTCGCGGGGTCGTACACCTAGTGACTCCGGATATTTACGACCTTGTAACGTAGTCTTTTTGAGCGAGAGTTTGCATCATGATCTCAGGAATGTTTGACGGAATATGCGC'

complement_table = {'A':'T','T':'A', 'G':'C','C':'G'}

print(complement_table['A'])

print(input_data_2)

#split the whole sequence into motifs of 4, 6, 8, 10, 12

list_of_four = []
index_dict_4 = {}
index_dict_6 = {} 
index_dict_8 = {}
index_dict_10 = {}
index_dict_12 = {}
#how to turn this into a simple loop?
for x,i in enumerate(input_data_2):
    #for the length of test string minus the length of the motif being checked, os that it doesn't go out of bounds
    if x < len(input_data_2)-3:
        #concatenate a string for each position in the input sequence + 3 following ones
        index_dict_4[x+1] = i+(input_data_2[x+1])+(input_data_2[x+2])+(input_data_2[x+3])
for x,i in enumerate(input_data_2):
    if x < len(input_data_2)-5:
        index_dict_6[x+1] = i+(input_data_2[x+1])+(input_data_2[x+2])+(input_data_2[x+3])+(input_data_2[x+4])+(input_data_2[x+5])
for x,i in enumerate(input_data_2):
    if x < len(input_data_2)-7:
        index_dict_8[x+1] = i+(input_data_2[x+1])+(input_data_2[x+2])+(input_data_2[x+3])+(input_data_2[x+4])+(input_data_2[x+5])+(input_data_2[x+6])+(input_data_2[x+7])  
for x,i in enumerate(input_data_2):
    if x < len(input_data_2)-9:
        index_dict_10[x+1] = i+(input_data_2[x+1])+(input_data_2[x+2])+(input_data_2[x+3])+(input_data_2[x+4])+(input_data_2[x+5])+(input_data_2[x+6])+(input_data_2[x+7])+(input_data_2[x+8])+(input_data_2[x+9])
for x,i in enumerate(input_data_2):
    if x < len(input_data_2)-11:
        index_dict_12[x+1] = i+(input_data_2[x+1])+(input_data_2[x+2])+(input_data_2[x+3])+(input_data_2[x+4])+(input_data_2[x+5])+(input_data_2[x+6])+(input_data_2[x+7])+(input_data_2[x+8])+(input_data_2[x+9])+(input_data_2[x+10])+(input_data_2[x+11])


list_of_answers = []
list_of_dictionaries = index_dict_4, index_dict_6, index_dict_8, index_dict_10, index_dict_12 

test_pal = 'ATGCAT'

def get_palindrome(sequence):
    newseq = [item for item in sequence[::-1]]

# for x,i in enumerate(index_dict_4):
#     #checking for palindromicity
#     first_condition = [complement_table[item] for item in index_dict_4[x+1]]
#     first_as_string = ''.join(first_condition)
#     second_condition = index_dict_4[x+1][::-1]
#     if first_as_string == second_condition:
#         list_of_answers.append(str(x+1)+' '+str(len(index_dict_4[x+1])))
        # list_of_answers.append(str(i,' ',str(len(index_dict_4[i]))))

dict_of_answers = {}
for n in list_of_dictionaries:
    for x,i in enumerate(n):
        #checking for palindromicity
        first_condition = [complement_table[item] for item in n[x+1]]
        first_as_string = ''.join(first_condition)
        second_condition = n[x+1][::-1]
        if first_as_string == second_condition:
            list_of_answers.append(str(x+1)+' '+str(len(n[x+1])))
            # list_of_answers.append(str(i,' ',str(len(index_dict_4[i]))))
            dict_of_answers[x+1] = str(len(n[x+1]))


print('\n')
print(index_dict_4)
print('\n')
print(index_dict_6)
print('\n')
print(index_dict_8)
print('\n')
print(index_dict_10)
print('\n')
print(index_dict_12)
print('answers:')
print('\n')
print(list_of_answers)

final_answer=''

for i in list_of_answers:
    final_answer += i
    final_answer += '\n'


savefile = open('REVP_result.txt', 'w')
#write the answe into the file as a string 
savefile.write(final_answer)
#filter which motifs are the same when reverse complemented
print(final_answer)
print(dict_of_answers)


for i in sorted(dict_of_answers.keys()):
    print(i,dict_of_answers[i])

dictionary_answer = ''

#write the answe into the file as a string 
for i in sorted(dict_of_answers.keys()):
    dictionary_answer += str(i)
    dictionary_answer += ' '
    dictionary_answer += dict_of_answers[i]
    dictionary_answer += '\n'

savefile = open('REVP_dict.txt', 'w')
savefile.write(dictionary_answer) 
print(dictionary_answer)

