fname = input("Enter the Name of the File : ")
infile = open(fname, 'r')
lines = 0
words = 0
characters = 0
for line in infile:
    wordslist = line.split()
    lines = lines + 1
    words = words + len(wordslist)
    characters = characters + len(line)
    
print("Total Lines : ", lines)
print("Total Words : ", words)
print("Total Characters : ",characters)
