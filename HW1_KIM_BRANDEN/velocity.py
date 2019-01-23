# author: Branden Kim
# assignment: HW1
# description: Calculate the velocity given distance and time

while True:
    try:
        distance = float(input('distance (in miles)? '))
        time_in_sec = float(input('time (in seconds)? '))
    except ValueError:
        print("Value must be a number")
    except KeyboardInterrupt:
        print()
        break
    else:
        time_in_hour = time_in_sec / 3600
        print(f'speed = {(distance / time_in_hour):.0f} miles / hour')
        break
