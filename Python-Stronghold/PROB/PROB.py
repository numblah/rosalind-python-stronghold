from lukas_data import FASTA

with open('rosalind_prob.txt', 'r') as file:
    input_data = file.readlines()

input_data = [item.rstrip('\n') for item in input_data]
print(input_data)   

DNA_string = input_data[0]
# split input into the GC GC contents 
list_of_gc = [float(item) for item in input_data[1].split(' ')]
list_of_gc
# write a function to calculate probability of a string based on the GC content
def string_probability_counter(string, GC_prob):
    """Returns probability of getting a particular DNA string with a known GC
    content (for the species or the broader string)"""
    import math
    probability = 1
    for i in string:
        if i == 'G' or i == 'C':
            probability *= GC_prob/2
        else:
            probability *= (1-GC_prob)/2

    return round(math.log10(probability),3)

string_probability_counter(DNA_string, list_of_gc[0])

results_list = [str(string_probability_counter(DNA_string, GC)) for GC in list_of_gc ]

print(results_list)
with open('results.txt', 'w') as file_results:
    file_results.write(' '.join(results_list))
# loop function through the GC contents
