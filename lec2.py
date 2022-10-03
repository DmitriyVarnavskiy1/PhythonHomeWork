colors = ['red', 'green', 'blue3']
data = open('file.txt', 'w')
data.writelines(colors)
data.close()

exit()
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()