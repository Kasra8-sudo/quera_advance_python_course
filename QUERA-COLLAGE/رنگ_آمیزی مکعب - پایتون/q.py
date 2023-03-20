def coloring(matrix):
    for item in matrix[1:len(matrix) - 1]:
        for col in item[1:len(item) - 1]:
            for row in range(1, len(col) - 1):
                col[row] = 0

    for i in range(len(matrix)):
        for j in matrix[i]:
            for k in range(len(j)):
                if j[k] != 0:
                    j[k] = 1
