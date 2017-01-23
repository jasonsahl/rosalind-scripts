readFile = open('input.txt', 'r')

count = 0
fileList = []

writeFile = open('output', 'w')

for line in readFile:
  if count % 2 == 1:
    writeFile.write(line)
  count += 1

readFile.close()
writeFile.close()

print 'sucess'
