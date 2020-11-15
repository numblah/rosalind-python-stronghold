#
import sys

f = open (sys.argv[1], "r")
task_files=f.readlines()
textline=task_files[0]
ranges=task_files[1].split()
print(ranges)
answer=textline[int(ranges[0]):int(ranges[1])+1]+' '+textline[int(ranges[2]):int(ranges[3])+1]
print(answer)
print()
f.close()git
#create a new file with the input
f2 = open('INI3_result.txt', 'w')
#write the answe into the file as a string 
f2.write(str(answer))


