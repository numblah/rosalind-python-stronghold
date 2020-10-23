#takes a file with 2 numbers and adds their squares
import sys
#open file (file name must be supplied by an argument)
f = open (sys.argv[1], "r")
#make a list by reading lines from the input file and splitting them by whitespaces
task_files=f.readline().split()
#define the answer ticker
answer=0
if 0<len(task_files)<=2:
	for i in task_files:
		if i.isdigit():
			answer+=int(i)**2
		else:
			print ("Only digits allowed as input")	
	print(answer)	
else:
	print("The input file must contain precicelly TWO numbers")		
f.close()
f2 = open('INI2_result.txt', 'w')
f2.write(str(answer))


