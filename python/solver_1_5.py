def make_grid(in_s):
    lines = in_s.split()
    grid = [list(map(int, l.replace('.', '0'))) for l in lines]
    return grid

def print_grid(grid, delimiter):
    s = [''.join(map(str, g)) for g in grid]
    print(delimiter.join(s))

def solve(grid):
    solve_sub(grid, 0)
    return grid

def solve_sub(grid, p):
    if p > 80:
        return True

    i = p // 9
    j = p % 9
    if grid[i][j] != 0:
        return solve_sub(grid, p + 1)

    for v in range(1, 10):
        grid[i][j] = v
        if is_valid_grid(grid, i, j):
            if solve_sub(grid, p + 1):
                return True

    # not found
    grid[i][j] = 0
    return False

def is_valid_grid(grid, i, j):
    # validate row block
    row = grid[i]
    is_valid_row = is_valid_block(row)

    # validate col block
    col = [grid[k][j] for k in range(9)]
    is_valid_col = is_valid_block(col)

    # validate square block
    sqr = [grid[3*(i//3) + k//3][3*(j//3) + k%3] for k in range(9)]
    is_valid_sqr = is_valid_block(sqr)

    return is_valid_row and is_valid_col and is_valid_sqr

def is_valid_block(block):
    d = [b for b in block if b != 0]
    return len(d) == len(set(d))

def main():
    in_grid = make_grid(input())
    ans_grid = solve(in_grid)
    print_grid(ans_grid, '\n')

if __name__ == '__main__':
    main()
