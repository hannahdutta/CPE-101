# Name:         Parth Ray
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Word Search
# Term:         Fall 2019

import wordsearch as ws

assert ws.reverse_string("parth") == "htrap"
assert ws.reverse_string("tacocat") == "tacocat"
assert ws.reverse_string("cat") == "tac"

assert ws.parse_word("CASEY WINDOWS LINUX PYTHON JAVA VIM", 0) == "CASEY"
assert ws.parse_word("CASEY WINDOWS LINUX PYTHON JAVA VIM", 2) == "LINUX"
assert ws.parse_word("CASEY WINDOWS LINUX PYTHON JAVA VIM", 3) == "PYTHON"

assert ws.transpose_string("ABCGITXYZ", 3) == "AGXBIYCTZ"
assert ws.transpose_string("ABCDEFGHIJKLMNOP", 4) == "AEIMBFJNCGKODHLP"
assert ws.transpose_string("part", 2) == "prat"
assert ws.transpose_string("ABCDEFGHIJKL", 3) == "ADGJBEHKCFIL" 

assert ws.forward_search("jflasdbvj", "v") == 7
assert ws.forward_search("abcdefghi", "f") == 5 
assert ws.forward_search("abcd", "c") == 2 

assert ws.backward_search("abcd", "c") == 1
assert ws.backward_search("jflasdbvj", "v") == 1
assert ws.backward_search("abcdefghi", "f") == 3

assert ws.upward_search("abcd", "c", 2) == 2
assert ws.upward_search("jflasdbvj", "v", 3) == 3 
assert ws.upward_search("abcdefghi", "f", 3) == 1

assert ws.downward_search("abcd", "c", 2) == 1
assert ws.downward_search("jflasdbvj", "v", 3) == 5 
assert ws.downward_search("abcdefghi", "f", 3) == 7 

