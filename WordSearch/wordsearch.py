# Name:         Parth Ray
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Word Search
# Term:         Fall 2019

def main():
    puzzle = (input("")).strip()
    words = (input("")).strip()
    width = int((len(puzzle) ** .5) // 1)
    display_puzzle(puzzle)
    word_count = words.count(" ") + 1
    for i in range(word_count):
        word = parse_word(words, i)
        if forward_search(puzzle, word) != -1:
            row = forward_search(puzzle, word) // width
            column = forward_search(puzzle, word) % width
            display_solution(word, "F", row, column, width)
        elif backward_search(puzzle, word) != -1:
            row = (len(puzzle) - 1 - backward_search(puzzle, word)) // width
            column = (len(puzzle) - 1 - backward_search(puzzle, word)) % width
            display_solution(word, "B", row, column, width)
        elif upward_search(puzzle, word, width) != -1:
            r = (len(puzzle) - 1 - upward_search(puzzle, word, width)) % width
            c = (len(puzzle) - 1 - upward_search(puzzle, word, width)) // width
            display_solution(word, "U", r, c, width)
        elif downward_search(puzzle, word, width) != -1:
            row = downward_search(puzzle, word, width) % width
            column = downward_search(puzzle, word, width) // width
            display_solution(word, "D", row, column, width)
             

def display_puzzle(puzzle):
    for i in range(0, len(puzzle), int(len(puzzle) ** .5)):
        word = ""
        for j in range(int(len(puzzle) ** .5)):
            word += puzzle[i + j]
        print(word)
    print()


def display_solution(word, direction, row, column, width):
    row = int(row)
    column = int(column)
    print(("{0:>{4}}: [{1}] ({2}, {3})").format(word, direction, row, column, width))


def forward_search(puzzle, word):
    location = puzzle.find(word)
    return location


def backward_search(puzzle, word):
    puzzle = reverse_string(puzzle)
    location = puzzle.find(word)
    return location

    
def upward_search(puzzle, word, width):
    puzzle = reverse_string(transpose_string(puzzle, width))
    location = puzzle.find(word)
    return location


def downward_search(puzzle, word, width):    
    puzzle = transpose_string(puzzle, width)
    location = puzzle.find(word)
    return location


def parse_word(words, position):
    word_at_position = ""
    spacecounter = 0
    for i in range(len(words)):
        if spacecounter == position and words[i].isalpha():
            word_at_position += words[i]
        elif " " == words[i]:
            spacecounter += 1
    return word_at_position


def reverse_string(chars):
    string = ""
    for i in range(len(chars) - 1, -1, -1):
        string += chars[i]
    return string


def transpose_string(chars, width):
    tpose = ""
    width = int(width)
    for i in range(0, width * (len(chars) // width), len(chars) // width):
        for j in range(len(chars) // width):
                tpose += chars[(j * width) + (i // (len(chars) // width))]
    return tpose


if __name__ == "__main__":
    main()
