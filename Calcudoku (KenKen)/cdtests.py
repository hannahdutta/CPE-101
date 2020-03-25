# Name:         Parth Ray
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Calcudoku
# Term:         Fall 2019

import calcudoku as cd

assert cd.transpose([[1, 2], [2, 1]]) == [[1, 2], [2, 1]]
assert cd.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8]
                        , [3, 6, 9]]
assert cd.transpose([[5, 20], [30, 10]]) == [[5, 30], [20, 10]]

assert cd.validate_line([1, 8, 9, 9]) == False 
assert cd.validate_line([1, 2, 3, 4]) == True 
assert cd.validate_line([1, 1, 1]) == False 

assert cd.validate_cage([[1, 2], [3, 4]], [4, 0, 2]) == True  
assert cd.validate_cage([[1, 2], [0, 4]], [4, 0, 2]) == True
assert cd.validate_cage([[4, 2], [5, 2]], [5, 1, 3]) == False

assert cd.check_lines([[5, 5], [1, 2]]) == False
assert cd.check_lines([[4, 2], [1, 2]]) == False
assert cd.check_lines([[4, 3], [1, 2]]) == True

assert cd.check_cages([[4, 3], [1, 2]], [[7, 0, 1], [3, 2, 3]]) == True
assert cd.check_cages([[4, 0], [1, 2]], [[5, 0, 1], [3, 2, 3]]) == True
assert cd.check_cages([[4, 3], [1, 2]], [[11, 0, 1, 2, 3]]) == False

assert cd.create_grid([[1, 2], [1, 3]]) == [[0, 0], [0, 0]]
assert cd.create_grid([[1, 8]]) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
assert cd.create_grid([[0, 1], [0, 0, 0]]) == [[0]]

assert cd.grid1d_to_2d([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [[1, 2, 3], 
                        [4, 5, 6], [7, 8, 9]]
assert cd.grid1d_to_2d([1]) == [[1]]
assert cd.grid1d_to_2d([1, 2, 3, 4]) == [[1, 2], [3, 4]] 