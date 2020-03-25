# Name:         Parth Ray
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Moonlander
# Term:         Fall 2019

def main():
    show_welcome()
    altitude = int(get_altitude())
    fuel_amount = get_fuel()
    velocity = 0
    acceleration = 0
    gravity = 1.62
    time = 0
    fuel_rate = 0
    while altitude > 0.00:
        if int(fuel_amount) > 0:
            display_state(time, altitude, velocity, fuel_amount, fuel_rate)
            fuel_rate = get_fuel_rate(fuel_amount)
            fuel_amount = update_fuel(fuel_amount, fuel_rate)
        else:
            fuel_rate = 0
            display_state(time, altitude, velocity, fuel_amount, fuel_rate)    
        time += 1
        acceleration = update_acceleration(gravity, fuel_rate)
        altitude = update_altitude(altitude, velocity, acceleration)
        velocity = update_velocity(velocity, acceleration)
    display_state(time, altitude, velocity, fuel_amount, fuel_rate)
    display_landing_status(velocity)


def show_welcome():
    print()
    print("Welcome aboard the Lunar Module Flight Simulator")
    print()
    print("   To begin you must specify the LM's initial altitude")
    print("   and fuel level.  To simulate the actual LM use")
    print("   values of 1300 meters and 500 liters, respectively.")
    print()
    print("   Good luck and may the force be with you!")
    print()


def get_altitude():
    alt = int(input("Enter the initial altitude of the LM (in meters): "))
    while alt > 9999 or alt < 1:
        print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
        alt = int(input("Enter the initial altitude of the LM (in meters): "))
    return alt


def get_fuel():
    fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
    while fuel <= 0:
        print("ERROR: Amount of fuel must be positive, please try again")
        fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
    return fuel


def get_fuel_rate(fuel_amount):
    fuel_rate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
    while fuel_rate < 0 or fuel_rate > 9:
        print("ERROR: Fuel rate must be between 0 and 9, inclusive")
        print()
        fuel_rate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
    fuel_rate = min(fuel_rate, fuel_amount)
    return fuel_rate    


def display_state(time, altitude, velocity, fuel_amount, fuel_rate):
    if time == 0:
        print()
        print("LM state at retrorocket cutoff")
    if altitude == 0:
        print()
        print("LM state at landing/impact")
    if fuel_amount <= 0 and altitude > 0:
        print("OUT OF FUEL - Elapsed Time:{0:4} Altitude: {1:7.2f} Velocity:{2:8.2f}".format(time, altitude, velocity))
    else:
        print("Elapsed Time: {0:4} s".format(time))
        print("{1:7} Fuel: {0:4} l".format(fuel_amount, ""))
        print("{1:7} Rate: {0:4} l/s".format(fuel_rate, ""))
        print("{1:3} Altitude: {0:7.2f} m".format(altitude, ""))
        print("{1:3} Velocity: {0:7.2f} m/s".format(velocity, ""))
        print()


def display_landing_status(velocity):
    if velocity >= -1 and velocity <= 0:
        print("Status at landing - The eagle has landed!")
    elif velocity > -10 and velocity < -1:
        print("Status at landing - Enjoy your oxygen while it lasts!")
    else:
        print("Status at landing - Ouch - that hurt!")


def update_acceleration(gravity, fuel_rate):
    acceleration = gravity * ((fuel_rate / 5) - 1)
    return acceleration


def update_altitude(altitude, velocity, acceleration):
    altitude = altitude + velocity + (acceleration / 2)
    if altitude < 0:
        altitude = 0
    return altitude


def update_velocity(velocity, acceleration):
    velocity = velocity + acceleration
    return velocity


def update_fuel(fuel_amount, fuel_rate):
    fuel_amount = fuel_amount - fuel_rate
    return fuel_amount
  

if __name__ == "__main__":
    main()

