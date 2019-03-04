f = open('all-mg-codes.txt')
l = open('labels.csv', 'w')
lines = []
for line in f:
    temp = line.split('\t')
    lines.append(temp)
for each in lines:
    img = each[0]
    new_line = img + ".jpg," + each[1] + "\n"
    l.write(new_line)
print("Done")