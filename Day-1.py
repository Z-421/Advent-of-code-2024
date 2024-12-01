
def problem1(first_column, second_column):
    sum = 0
    for i in range(len(first_column)):
        m1 = min(first_column)
        m2 = min(second_column)
        res = m1 - m2
        if (res <= 0):
            res = -1 * res
        sum = sum + res
        first_column.remove(m1)
        second_column.remove(m2)


    print(sum)


def problem2(first_column, second_column):
    sum = 0
    for elm in first_column:
        c = 0
        for elm2 in second_column:
            if elm == elm2:
                c += 1
        res = elm * c
        sum += res
    
    print(sum)


first_column = []
second_column = []

with open('txt.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        first_column.append(num1)
        second_column.append(num2)

# i called problem2 first because i will remove each element from the list in problem1

problem2(first_column, second_column)
problem1(first_column, second_column)