def make_grid(in_s):
    line = in_s.replace(' ', '')
    grid = list(map(int, line.replace('.', '0')))
    return grid

def print_grid(grid, delimiter):
    lines = [grid[9*i:9*i + 9] for i in range(9)]
    s = [''.join(map(str, l)) for l in lines]
    print(delimiter.join(s))

def solve(grid):
    solve_sub(grid, 0)
    return grid

def solve_sub(grid, p):
    if p > 80:
        return True

    if grid[p] != 0:
        return solve_sub(grid, p + 1)

    for v in possible_numbers(grid, p):
        grid[p] = v
        if is_valid_grid(grid, p) and solve_sub(grid, p + 1):
            return True

    # not found
    grid[p] = 0
    return False

def row(grid, p):
    offset_i = 9*(p//9)
    return grid[offset_i:offset_i + 9]

def column(grid, p):
    offset_j = p%9
    return [grid[9*k + offset_j] for k in range(9)]

def square(grid, p):
    offset_i = 9*(p//9)
    offset_j = p%9
    return [grid[27*(offset_i//27) + 9*(k//3) + 3*(offset_j//3) + k%3] for k in range(9)]

def is_valid_grid(grid, p):
    is_valid_row = is_valid_block(row(grid, p))
    is_valid_col = is_valid_block(column(grid, p))
    is_valid_sqr = is_valid_block(square(grid, p))

    return is_valid_row and is_valid_col and is_valid_sqr

def is_valid_block(block):
    d = [b for b in block if b != 0]
    return len(d) == len(set(d))

def possible_numbers(grid, p):
    return {i for i in range(1, 10)} - fixed_numbers(grid, p)

def fixed_numbers(grid, p):
    return set(row(grid, p)) | set(column(grid, p)) | set(square(grid, p))

def main():
    in_grid = make_grid(input())
    ans_grid = solve(in_grid)
    print_grid(ans_grid, '\n')

if __name__ == '__main__':
    main()
