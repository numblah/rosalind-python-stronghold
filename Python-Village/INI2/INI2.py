#takes a file with 2 numbers and adds their squares
import sys
#open file (file name must be supplied by an argument)
f = open (sys.argv[1], "r")
#make a list by reading lines from the input file and splitting them by whitespaces
task_files=f.readline().split()
#define the answer ticker
answer=0
#check if the list only contains two items
if 0<len(task_files)<=2:
	#iterate over the items
	for i in task_files:
		#make sure that the item is a digit
		if i.isdigit():
			#add the square to the ticker
			answer+=int(i)**2
		#warn the user that the item is not a digit	
		else:
			print ("Only digits allowed as input")
	#print the final anser to terminal			
	print(answer)	
#warn the user that wrong number of items was input	
else:
	print("The input file must contain precicelly TWO numbers")	
#close the input file		
f.close()
#create a new file with the input
f2 = open('INI2_result.txt', 'w')
#write the answe into the file as a string 
f2.write(str(answer))


