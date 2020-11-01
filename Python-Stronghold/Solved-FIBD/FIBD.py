#A re-write of Python-Stronghold-FIB to account for dying rabbits 

num_kids=1
num_adults=0

 


#define the number of individuals (n) to start with and the number of generations to run for (k) 
n=85 # number of generations 
m=17 # survival time
k=1 # keep the litter statistic but leave it at 1
#expected remainder total = 3 

ads=[]
kids=[]
adults_tracker=[]
for i in range(n):

	#count number of progeny/adults before dying starts
	if i <m:
		#initial step that starts counting adults and kids (the condition could as well be "len(kids) == 0")
		if len(ads) ==0:
			ads.append(num_adults)
			kids.append(num_kids)
			adults_tracker.append(num_adults)
		#if adults exist (i.e. there are not zero adults)	
		elif num_adults != 0:
			
			num_kids=ads[i-1]*k
			
			num_adults=kids[i-1]+ads[i-1]
			
			print("kids", num_kids, "adults", num_adults)
			#keep each generation in a list (for calculating the next generation in the next cycle of the loop)
			ads.append(num_adults)
			kids.append(num_kids)
			adults_tracker.append(kids[i-1])
		#the second step where the one starting kid turns into an adult (making kids revert back to zero)	
		else:
			num_adults=1
			num_kids=0
			ads.append(num_adults)
			kids.append(num_kids)
			adults_tracker.append(num_adults)
	#once dying has started start calculating the number of adults by subtracting the number of new kids 'm' generations ago. 		
	else:
		num_kids=ads[i-1]*k
			
		num_adults=kids[i-1]+ads[i-1]-kids[i-m]
			
		print("kids", num_kids, "adults", num_adults)
		#keep each generation in a list (for calculating the next generation in the next cycle of the loop)
		ads.append(num_adults)
		kids.append(num_kids)
		adults_tracker.append(kids[i-1])

print("adults")
print(ads)
print("kids")
print(kids)
print('new adults')
print(adults_tracker)


print("final answer")
print(ads[n-1]+kids[n-1])
