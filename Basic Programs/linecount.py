#counting number of line nd word from a file
import sys
filename = sys.argv[1]
filehandler = open(filename,'r')
count = 0
for line in filehandler.read():
    count = count +1
    print(line)
 