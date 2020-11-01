num_kids=1
num_adults=0

#define the number of individuals (n) to start with and the number of generations to run for (k) 
n=36
k=4

ads=[]
kids=[]
for i in range(n):
	#initial step that starts counting adults and kids (the condition could as well be "len(kids) == 0")
	if len(ads) ==0:
		ads.append(num_adults)
		kids.append(num_kids)

	#if adults exist (i.e. there are not zero adults)	
	elif num_adults != 0:
		#define the number of kids in this generation as number of adults from the previous generation multiplied by 'k' the litter number
		num_kids=ads[i-1]*k
		#the number of adults in this generation is the number of adults in the previous generation together with the number of kids in the previous generation
		#assumption: adults don't die
		num_adults=kids[i-1]+ads[i-1]
		#print each geneartions numbers for tracking
		print("kids", num_kids, "adults", num_adults)
		#keep each generation in a list (for calculating the next generation in the next cycle of the loop)
		ads.append(num_adults)
		kids.append(num_kids)

	#the second step where the one starting kid turns into an adult (making kids revert back to zero)	
	else:
		num_adults=1
		num_kids=0
		ads.append(num_adults)
		kids.append(num_kids)

	

print("adults")
print(ads)
print("kids")
print(kids)



print(ads[n-1]+kids[n-1])


# exp: 1850229480761
# mine:   8878212019
# rebel:   178956971


#:       1323839213083
#rebel: 875089148811941

# 123280631024265 correct for 36, 4
# 123280631024265
#   3048504677680