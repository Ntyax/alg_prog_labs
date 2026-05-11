def solve_ijones():
    try:
        with open('ijones_in.txt', 'r') as f:
            lines = f.readlines()
            if not lines:
                return
            
            w, h = map(int, lines[0].split())
            grid = [line.strip() for line in lines[1:h+1]]

        dp = [[0] * w for _ in range(h)]
        
        char_sums = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        for r in range(h):
            dp[r][0] = 1

        for c in range(w):
            if c > 0:
                for r in range(h):
                    letter = grid[r][c]
                    
                    ways = dp[r][c-1]
                    
                    ways += char_sums[letter]
                    
                    if grid[r][c-1] == letter:
                        ways -= dp[r][c-1]
                    
                    dp[r][c] = ways

            for r in range(h):
                char_sums[grid[r][c]] += dp[r][c]

        if h == 1:
            result = dp[0][w-1]
        else:
            result = dp[0][w-1] + dp[h-1][w-1]

        with open('ijones.out', 'w') as f:
            f.write(str(result))

    except FileNotFoundError:
        print("Файл ijones_in.txt не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    solve_ijones()