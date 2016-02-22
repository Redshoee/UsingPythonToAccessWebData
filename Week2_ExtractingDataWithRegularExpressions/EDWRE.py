import re
data = open('regex_sum_248858.txt')
y=0
for line in data:
    line = line.rstrip()
    stuff =re.findall('([0-9]+)',line)
    if len(stuff) <1 : continue
    for i in stuff:
        num = float(i)
        y = y + num
        
print 'Ends with : %d' %num
print 'The sum is : %d' %y

