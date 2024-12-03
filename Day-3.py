import re

def problem1(f):
    string = r"mul\((\d{1,3}),(\d{1,3})\)"
    nums = re.finditer(string, f)
    sum = 0
    for elm in nums:
        res = int(elm.group(1))*int(elm.group(2))
        sum += res
    
    print(sum)

def problem2(f):
    string = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    sum2 = 0
    x = True
    maches = re.finditer(string, f)
    for m in maches:
        if m.group(0) == "do()":
            x = True
        elif m.group(0) == "don't()":
            x = False
        elif m.group(1) and m.group(2):
            if x:
                res = int(m.group(1))*int(m.group(2))
                sum2 += res
            

    print(sum2)

with open('txt.txt', 'r') as file:
    f = file.read()
    problem1(f)
    problem2(f)
