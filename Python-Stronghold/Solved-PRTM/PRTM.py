# with open('protein_mass_table.txt', 'r') as myfile:
#   data = myfile.readlines()

import sys
data = [line.rstrip() for line in open('protein_mass_table.txt')]
input_data = [line.rstrip() for line in open(sys.argv[1])]
#need to select [0] as it is a string within a list
input_data_2 = [char for char in input_data[0]]

mass_table = []

for i in data:
    mass_table.append(i.split('   '))
list_of_amino_refs = []
list_of_amino_mass = []
for i in mass_table:
    list_of_amino_refs.append(i[0])

for i in mass_table:
    list_of_amino_mass.append(float(i[1]))

mass_table_dict = {list_of_amino_refs[i]: list_of_amino_mass[i] for i in range(len(list_of_amino_mass))}     

answer = 0 
for i in input_data_2:
    answer += mass_table_dict[i]

print(round(answer,3))

savefile = open('PRTM_result.txt', 'w')
#write the answe into the file as a string 
savefile.write(str(round(answer,3)))

# print(mass_table)

# print("\n")
# print("love")

# print('cut')