def zigzag_traverse(matrix):
    if not matrix or not matrix[0]:
        return []
    n = len(matrix)
    m = len(matrix[0])
    result = []

    for d in range(n + m - 1):
        diagonal = []
        if d % 2 == 0:
            row = min(d, n - 1)
            col =  d - min(d, n - 1)
            while row >= 0 and col < m:
                diagonal.append(matrix[row][col])
                row = row - 1
                col =  col + 1
        else:
            col = min(d, m - 1)
            row =  d - min(d, m - 1)
            while row < n and col >= 0:
                diagonal.append(matrix[row][col])
                row = row + 1
                col = col - 1
        result.extend(diagonal)
    return result

def get_positions(n, m):
    return zigzag_traverse([[(i, j) for j in range(m)] for i in range(n)])


def get_time(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    rd, cd = abs(r2 - r1), abs(c2 - c1)
    return 2 * rd if rd == cd and rd > 0 else rd + cd

n = int(input("Кількість рядів: "))
m = int(input("Кількість стовпців: "))

car_row = int(input("Рядок машини: "))
car_col = int(input("Стовпець машини: "))
car = (car_row, car_col)

positions = get_positions(n, m)
car_idx = positions.index(car)

time_first = sum(get_time(positions[i], positions[i + 1]) for i in range(car_idx))
time_end = sum(get_time(positions[i], positions[i + 1]) for i in range(car_idx, len(positions) - 1))

positions_reverse = positions[::-1]
car_idx_reverse = len(positions_reverse) - 1 - car_idx
time_second = sum(get_time(positions_reverse[i], positions_reverse[i + 1]) for i in range(car_idx_reverse))
print(f"Час до трупа {time_first}")

print(f"Час до прибирання крові {time_second+time_end}")