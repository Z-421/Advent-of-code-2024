with open('txt.txt', 'r') as file:
    lines = file.readlines()
    sum_part1 = 0
    sum_part2 = 0

    # Problem 1
    for line in lines:
        sum_part1 += line.count("XMAS") + line.count("SAMX")
    

    for col in range(len(lines)):
        column = ''.join(line[col] for line in lines)
        sum_part1 += column.count("SAMX") + column.count("XMAS")
    

    diagonals = []

    for i in range(len(lines)):
        diagonal = ''
        row = i
        col = 0
        while row < len(lines) and col < len(lines[row]):
            diagonal += lines[row][col]
            row += 1
            col += 1
        diagonals.append(diagonal)
    
    for i in range(1, len(lines[0])):
        diagonal = ''
        row = 0
        col = i
        while row < len(lines) and col < len(lines[row]):
            diagonal += lines[row][col]
            row += 1
            col += 1
        diagonals.append(diagonal)
    
    for i in range(len(lines)):
        diagonal = ''
        row = i
        col = len(lines[0]) - 1
        while row < len(lines) and col >= 0:
            if col < len(lines[row]):
                diagonal += lines[row][col]
            row += 1
            col -= 1
        diagonals.append(diagonal)
    
    for i in range(len(lines[0])-2, -1, -1):
        diagonal = ''
        row = 0
        col = i
        while row < len(lines) and col >= 0:
            diagonal += lines[row][col]
            row += 1
            col -= 1
        diagonals.append(diagonal)
    
    for d in diagonals:
        sum_part1 += d.count("XMAS") + d.count("SAMX")

    
    # Problem 2
    count = 0
    for i in range(1, len(lines)-1):
        for k in range(1, len(lines[0])-1):
            if lines[i][k] == "A":
                if (((lines[i-1][k-1] == "M" ) and (lines[i-1][k+1] == "S")) and ((lines[i+1][k+1] == "S") and (lines[i+1][k-1] == "M"))) or (((lines[i-1][k-1] == "S" ) and (lines[i-1][k+1] == "M")) and ((lines[i+1][k+1] == "M") and (lines[i+1][k-1] == "S"))) or (((lines[i-1][k-1] == "M" ) and (lines[i-1][k+1] == "M")) and ((lines[i+1][k+1] == "S") and (lines[i+1][k-1] == "S"))) or (((lines[i-1][k-1] == "S" ) and (lines[i-1][k+1] == "S")) and ((lines[i+1][k+1] == "M") and (lines[i+1][k-1] == "M"))):
                    count += 1
        
    sum_part2 = count
    print(sum_part1)
    print(sum_part2)