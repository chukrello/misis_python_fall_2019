def trip(line, column, field):
    test_field = [[0 for val in line] for line in field]
    test_field[0][0] = 1
    for i in range(line):
        for j in range(column):
            if field[i][j] == 0 or test_field == 0:
                continue
            else:
                if i + field[i][j] < line and j + field[i][j] < column:
                    test_field[i + field[i][j]][j] += test_field[i][j]
                    test_field[i][j + field[i][j]] += test_field[i][j]
                elif i + field[i][j] < line and j + field[i][j] >= column:
                    test_field[i + field[i][j]][j] += test_field[i][j]
                elif i + field[i][j] >= line and j + field[i][j] < column:
                    test_field[i][j + field[i][j]] += test_field[i][j]
    return str(test_field[line - 1][column - 1])




