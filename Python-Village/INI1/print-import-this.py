"""
Type in the file name  (.txt) as the argument to save the output of the message received from running "import this"



"""
#import the all important system module
import sys
#initiate the capture of standard output into a file defined as an argument when launching the script
#"w" for write mode
sys.stdout = open(sys.argv[1], "w")
#a python easter egg generating a fun import message
import this
#conclude the standard out 'recording' and complete the file
sys.stdout.close()
