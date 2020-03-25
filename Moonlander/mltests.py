# Name:         Parth Ray
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Moonlander
# Term:         Fall 2019

import moonlander

assert moonlander.update_acceleration(1.62, 5) == 0 
assert abs(moonlander.update_acceleration(1.62, 9) - 1.296) <= 1e-5
assert abs(moonlander.update_acceleration(1.62, 3) - -0.648) <= 1e-5

assert moonlander.update_altitude(7.4, 5.7, 7.3) == 16.75
assert moonlander.update_altitude(8.9, 1.2, 2.3) == 11.25
assert moonlander.update_altitude(1.6, -7.2, 4.2) == 0

assert moonlander.update_velocity(3.2, 5.3) == 8.5
assert moonlander.update_velocity(6.2, 7.2) == 13.4
assert moonlander.update_velocity(3.62, 4.55) == 8.17 

assert moonlander.update_fuel(37, 5) == 32 
assert moonlander.update_fuel(28, 2) == 26
assert moonlander.update_fuel(10, 9) == 1
