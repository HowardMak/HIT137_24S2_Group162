def draw_square(n):
    m = [[" "] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if r == 0 or r == (n - 1):
                m[r][c] = '*'
            if c == 0 or c == (n - 1):
                m[r][c] = '*'
    return "\n".join([" ".join(row) for row in m])


if __name__ == '__main__':
    print(draw_square(4))
