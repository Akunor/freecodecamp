# start of main.py

def launch_fuel(payload):
    fuel = 0
    remaining_weight = payload

    while remaining_weight >= 1:
        new = remaining_weight/5
        fuel += new
        remaining_weight = new

    final_fuel = round(fuel, 1)

    return final_fuel

'''
# Better solution using result of the infinite geometric series = 1/4:

def launch_fuel(payload):
    fuel = round(payload/4, 1)

    return fuel

'''

# end of main.py