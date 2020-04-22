import sys
source=sys.argv[1]
csvfilename = open(source, 'r')
file = 1
lines_count = 0
current  = open('chunk-' + str(file)+'.csv', 'at') 
for line in csvfilename:
	current.write(line) #appending to current file buffer
	current.flush() #clear the buffer and writes to file (affects speed)
	lines_count +=1 
	if lines_count == 10**6:
		current.close()
		print('file '+ str(file)+ ' completed')
		file+=1
		current  = open('chunk-' + str(file)+'.csv', 'at')
		lines_count = 0 
print('Done!')
