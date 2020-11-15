with open('RNA_codon_table.txt', 'r') as file:
       data = file.read()

data.split()

#scans the data and returns two lists one for codons the other for matching amino acids
list_of_codons = [item for item in data.split() if len(item) == 3]
list_of_amino_acids = [item for item in data.split() if len(item) != 3]

RNA_codon_dict = {}

#create two variants of of ziped lists
#the first one loses data for repeating amino_acid:codon pairs
items = zip(list_of_amino_acids,list_of_codons)
#making a codon:amino_acid dictionary avoids this problem
items2 = zip(list_of_codons, list_of_amino_acids)

#create two variants of of ziped lists
RNA_codon_dict = {key:value for (key,value) in items}
RNA_codon_dict2 = {key:value for (key,value) in items2}

dictionary_number_of_codonds_per_acid = {}
for i in set(list_of_amino_acids):
    print(i,'-----------', list(RNA_codon_dict2.values()).count(i))
    dictionary_number_of_codonds_per_acid[i] = list(RNA_codon_dict2.values()).count(i)



def codon_posibility_counter(protein_string):
    #note may bug out if sequences put in not as capitals or if 
    answer = 1 

    for i in protein_string:
        answer *= dictionary_number_of_codonds_per_acid[i]
    
    answer *= dictionary_number_of_codonds_per_acid['Stop']
    return answer % 1000000

codon_posibility_counter('MPAKYKHWINQCMSGTYHLTIERDIFHCPYRNYTEDTAIFPGIVYEPDYHAFHPSMEYYSKIEPNILSPGSFCTENVWAVEGELRGWWHPWMMTPIMCDWGFGPPVWKSSCVGMREIMCKTSHLCCKTCRDRVAGSYPWYTLLCWLPSPNTYCRREGCCKLLGFRKTTQKFRFDKIECVMYDASKRSEVYYLPMVTFKIQWAWFRHCYQHNSMECGGELFFPCDAHHDRRAPTMSDMFARNVTCVNCVTFEASVHDFLEFYYDWWPEVYEVSFLKTMYQQHNNHMFDRQTYQDLMNFDHFWVGTYSAGSMKYGDHKLDFTMFPERQATKEWSNGGHEMQNICLTEMDWRHEPDFWCAMDENFGVGSFAHFNCDCDRWKMHHQLDGVMESGVCHWPWKRTQDCPDHKKKEYCWDADEALDLRKDMTCKWVVNMEQNYEENCNMLVRQAKGHRQQFYVKRALEKRKSGTSPSQVSCWHWSMSMEVQPYSESPWPHACISTMIMKHKGMHGHPRRIGHPVFIAKLLGHQVKPMVLSQIKEVWTAVWPDSVIFQYLCGSYFQHFVEPNFDWEFDKLVNRMCIPYKFLPWRGFVNLWYKFERPIFHPPLQHIVMREWKGRVQCPELAWLASNCGWHHYPARWVMGEQGWNKRRQDLVSPQTDIWEHWGAVDYPTPSLLLLCHFTIRAFAWTGHQHDKKAHMAQADCMQDEKNTDKDSAKYYITYDFLTIGKSQMADIHRYNSKHQNEAEKKIPIDDHDVRHQTTFQPGTMVSFNNKKSFFYTWMWYMLTEGHWKWRMLNPANISPPFNTMGQIPREHNKVLQSGLREVHIHAKWCWFCWRLPMAFPKTHEWEQHVGTCMISPQRDYFYQMYSFSRQRGPHKHYEGRFNLLAWYTAINHWNHVHMAVMMWNMHHYMLQSWDNDSVWCLIEECTGMDSDSTQQVTVGSAHNRWSDLADVIWHCKAVRQVKNCADVLENAKGHCWCYRIMILSTMRTESEPKTFPTI')
