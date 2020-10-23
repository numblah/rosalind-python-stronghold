num_kids=1
num_adults=0

#define the number of individuals (n) to start with and the number of generations to run for (k) 
n=36
k=4

ads=[]
kids=[]
for i in range(n):
	if len(ads) ==0:
		ads.append(num_adults)
		kids.append(num_kids)
	elif num_adults != 0:
		num_kids=ads[i-1]*k
		num_adults=kids[i-1]+ads[i-1]

		print("kids", num_kids, "adults", num_adults)
		ads.append(num_adults)
		kids.append(num_kids)
		
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