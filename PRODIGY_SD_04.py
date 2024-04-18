def is_valid_move(grid, row, col, number) :
	for x in range ( 9 ) :
		if grid[row][x] == number :
			return False
	for x in range ( 9 ) :
		if grid[col][x] == number :
			return False

	corner_row = row - row % 3
	corner_col = col - col % 3
	for x in range ( 3 ) :
		for y in range ( 3 ) :
			if grid[corner_row + x][corner_col + y] == number :
				return False

	return True


def solve(grid, row, col) :
	if col == 9 :
		if row == 8 :
			return True
		row += 1
		col = 0

	if grid[row][col] > 0 :
		return solve ( grid, row, col + 1 )

	for num in range ( 1, 10 ) :

		if is_valid_move ( grid, row, col, num ) :

			grid[row][col] = num

			if solve ( grid, row, col + 1 ) :
				return True

			grid[row][col] = 0

		return False


grid = [[1, 4, 3, 9, 8, 6, 2, 5, 7],
       [6, 7, 9, 4, 2, 5, 3, 8, 1],
       [2, 8, 5, 7, 3, 1, 6, 9, 4],
       [9, 6, 2, 3, 5, 4, 1, 7, 8],
       [3, 5, 7, 6, 1, 8, 9, 4, 2],
       [4, 1, 8, 2, 7, 9, 5, 6, 3],
       [8, 2, 1, 5, 6, 7, 4, 3, 9],
       [7, 9, 6, 1, 4, 3, 8, 2, 5],
       [5, 3, 4, 8, 9, 2, 7, 1, 6]]

if solve ( grid, 0, 0 ) :
	for i in range ( 9 ) :
		for j in range ( 9 ) :
			print ( grid[i][j], end=" " )
		print ( )
else :
	print ( "No solution for sudoku" )
