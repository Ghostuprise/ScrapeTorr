import re
import fileinput
for each_line in fileinput.input("output.json"):
	matchLine = re.search ('tr=udp.*\..*\..*%', each_line)
	each_line.replace('%','xxxx')
	if matchLine is not None:
		print matchLine.group()
	else:
		continue

