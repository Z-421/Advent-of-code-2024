def problem1(arr):
    res1 = 0
    if (sorted(arr) == arr) or (sorted(arr, reverse=True) == arr):
        c = 0
        for elm1, elm2 in zip(arr, arr[1:]):
            if ((elm1 - elm2 >= 1) and (elm1 - elm2 <= 3)) or ((elm1 - elm2 >= -3) and (elm1 - elm2 <= -1)):
                c += 1
                if c == len(arr)-1:
                    res1  += 1

    return res1

arr = []


file = open("txt.txt", 'r')
res = 0
res2 = 0
for each_l in file:
    arr = list(map(int, each_l.split(" ")))
    m = problem1(arr)
    if m == 0:
        for i in range(len(arr)):
            elm = arr.pop(i)
            m = problem1(arr)
            if m == 1:
                res2 += 1
                break
            else:
                arr.insert(i, elm)
    else:
        res = res + m
        




file.close()
    

print(f"first problem = {res}")
print(f"second problem = {res2 + res}")