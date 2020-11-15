import lukas_data
import numpy as np

input_frame = lukas_data.FASTA('rosalind_cons.txt')

list_of_frames = list(input_frame['seq'])

list_of_one = [char for char in list_of_frames[1]]

#turn the array into a list of lists
list_of_one_list = []
for x,i in enumerate(list_of_frames):
    list_of_one_list.append(([char for char in list_of_frames[x]]))

sequence_matrix = np.array(list_of_one_list )

list(sequence_matrix[:,0]).count('A')

#len of the matrix is the same as the number of columns
As = []
Cs = []
Gs = []
Ts = []
consensus = []

#a function to find the most common item in the list, to be used for consensus building
#may want to look into the behaviour when equal amounts of bases are present
def most_frequent(List): 
    return max(set(List), key = List.count) 

for i in range(len(sequence_matrix[0])):
    As.append(list(sequence_matrix[:,i]).count('A'))
    Cs.append(list(sequence_matrix[:,i]).count('C'))
    Gs.append(list(sequence_matrix[:,i]).count('G'))
    Ts.append(list(sequence_matrix[:,i]).count('T'))
    consensus.append(most_frequent(list(sequence_matrix[:,i])))
    # if list(sequence_matrix[:,i]).count('A') > list(sequence_matrix[:,i]).count('C') and list(sequence_matrix[:,i]).count('G') and list(sequence_matrix[:,i]).count('T'):
    #     consensus.append('A')
    # elif list(sequence_matrix[:,i]).count('T') > list(sequence_matrix[:,i]).count('A') and list(sequence_matrix[:,i]).count('G') and list(sequence_matrix[:,i]).count('C'):
    #     consensus.append('T')
    # elif list(sequence_matrix[:,i]).count('C') > list(sequence_matrix[:,i]).count('A') and list(sequence_matrix[:,i]).count('G') and list(sequence_matrix[:,i]).count('T'):  
    #     consensus.append('C')
    # else:
    #     consensus.append('G')

print('As',As)
print('Cs',Cs)
print('Gs',Gs)
print('Ts',Ts)
print(consensus)
print('\n')


with open('result.txt', 'w') as the_file:
    the_file.write(''.join(consensus)+'\n')
    the_file.write('A: '+' '.join([str(item) for item in As])+'\n')
    the_file.write('C: '+' '.join([str(item) for item in Cs])+'\n')
    the_file.write('G: '+' '.join([str(item) for item in Gs])+'\n')
    the_file.write('T: '+' '.join([str(item) for item in Ts])+'\n')
    