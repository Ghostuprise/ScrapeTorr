infile = open('./matched')
outfile = open('./replace', 'w')

replacements = {'tr=udp%3A%2F%2F':'', '%3A1337&':',' , '%3A6969&':','}

for line in infile:
    for src, target in replacements.iteritems():
        line = line.replace(src, target)
    outfile.write(line)
infile.close()
outfile.close()

infile = open('./replace')
outfile = open('./replace_out', 'w')

replacements = {'%':''}

for line in infile:
    for src, target in replacements.iteritems():
        line = line.replace(src, target)
    outfile.write(line)
infile.close()
outfile.close()

