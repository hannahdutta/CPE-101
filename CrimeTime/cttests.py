# Name:         Parth Ray
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Crime Time   
# Term:         Fall 2019
import crimetime as ct

c1 = ct.Robbery(1234)
c2 = ct.Robbery(63)
c3 = ct.Robbery(1234)
c4 = ct.Robbery(42)
c5 = ct.Robbery(24)
c6 = ct.Robbery(22)
c3.time = 1230
c2.time = 0
c4.time = 1302
c5.time = 102
c6.time = 30

assert (c1 == c2) == False
assert (c1 == c4) == False
assert (c1 == c3) == True

assert str(c1) == "1234\tNone\n"
assert str(c2) == "63\t12:00AM\n"
assert str(c3) == "1234\t12:30PM\n"
assert str(c4) == "42\t1:02PM\n"
assert str(c5) == "24\t1:02AM\n"
assert str(c6) == "22\t12:30AM\n"

assert ct.find_crime([ct.Robbery(1), ct.Robbery(2), ct.Robbery(5)], 5) == 2
assert ct.find_crime([ct.Robbery(1), ct.Robbery(2), ct.Robbery(5)], 20) == -1
assert ct.find_crime([ct.Robbery(1), ct.Robbery(4), ct.Robbery(5)], 1) == 0

x = ct.Robbery(1)
y = ct.Robbery(2)
z = ct.Robbery(3)
c = ct.Robbery(5)
x.convert_time("12:41")
y.convert_time("05:36")
z.convert_time("14:52")
assert x.time == 1241
assert y.time == 536
assert z.time == 1452
c.convert_time("14:52")
assert c.__lt__(z) == False
assert x.__lt__(y) == False
assert y.__lt__(z) == True

r1 = [ct.Robbery(1), ct.Robbery(4), ct.Robbery(2), ct.Robbery(3)]
r2 = [ct.Robbery(5), ct.Robbery(4), ct.Robbery(6), ct.Robbery(3)]
r3 = [ct.Robbery(1), ct.Robbery(4), ct.Robbery(2), ct.Robbery(3)]
r3[0].convert_time("01:23")
r3[1].convert_time("10:30")
r3[2].convert_time("11:22")
r3[3].convert_time("01:23")
ct.sort_crimes(r1, "id")
ct.sort_crimes(r2, "id")
ct.sort_crimes(r3, "time")
assert r1 == [ct.Robbery(1), ct.Robbery(2), ct.Robbery(3), ct.Robbery(4)]
assert r2 == [ct.Robbery(3), ct.Robbery(4), ct.Robbery(5), ct.Robbery(6)]
assert r3 == [ct.Robbery(1), ct.Robbery(3), ct.Robbery(4), ct.Robbery(2)]
