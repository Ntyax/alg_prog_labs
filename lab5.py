import ast
import os
import sys

sys.setrecursionlimit(2000)

def flood_fill(matrix, r, c, target_color, replacement_color):
    rows = len(matrix)
    cols = len(matrix[0])

    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    
    if matrix[r][c] != target_color or matrix[r][c] == replacement_color:
        return

    matrix[r][c] = replacement_color

    flood_fill(matrix, r + 1, c, target_color, replacement_color)
    flood_fill(matrix, r - 1, c, target_color, replacement_color)
    flood_fill(matrix, r, c + 1, target_color, replacement_color)
    flood_fill(matrix, r, c - 1, target_color, replacement_color)

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_path, 'input.txt')
    output_path = os.path.join(base_path, 'output.txt')

    try:
        if not os.path.exists(input_path):
            print(f"Помилка: Файл не знайдено за шляхом {input_path}")
            return

        with open(input_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

        if len(lines) < 4:
            print("Помилка: Недостатньо даних у файлі input.txt")
            return

        start_r, start_c = map(int, lines[1].split(','))
        
        replacement_color = lines[2].replace("'", "").replace('"', "")

        matrix_raw = "".join(lines[3:])
        if not matrix_raw.endswith(']'):
             matrix_raw = matrix_raw.rstrip(',')
             
        matrix = ast.literal_eval(f"[{matrix_raw}]")

        target_color = matrix[start_r][start_c]

        flood_fill(matrix, start_r, start_c, target_color, replacement_color)

        with open(output_path, 'w', encoding='utf-8') as f:
            for i, row in enumerate(matrix):
                suffix = "," if i < len(matrix) - 1 else ""
                f.write(f"{row}{suffix}\n")
        
        print(f"Готово! Результат збережено в: {output_path}")

    except Exception as e:
        print(f"Виникла помилка: {e}")

if __name__ == "__main__":
    main()