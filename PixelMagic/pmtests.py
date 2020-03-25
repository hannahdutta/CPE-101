# Name:         Parth Ray
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Pixel Magic
# Term:         Fall 2019
import pixelmagic as pm

assert pm.fade_image([[20, 30, 200]], 7, 3, 3, 3) == [[4, 6, 40]]
assert pm.fade_image([[20, 30, 200]], 7, 3, 3, 9) == [[10, 15, 105]]
assert pm.fade_image([[20, 30, 200], [255, 255, 4]], 7, 3, 3, 9) == [
    [10, 15, 105], [152, 152, 2]]

assert pm.blur_image([[20, 20, 20]], 1, 0) == [[20, 20, 20]]
assert pm.blur_image([[20, 20, 20], [40, 40, 40]], 1, 1) == [[30, 30, 30],
 [30, 30, 30]]
assert pm.blur_image([[40, 40, 40]], 1, 1) == [[40, 40, 40]]