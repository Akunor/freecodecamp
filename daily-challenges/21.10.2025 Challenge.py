# start of main.py

def adjust_thermostat(current_f, target_c):
    target_f = (target_c * 1.8) + 32
    action = ''
    if current_f < target_f:
        action = f'Heat: {(target_f - current_f):.1f} degrees Fahrenheit'
    elif current_f > target_f:
        action = f'Cool: {(current_f - target_f):.1f} degrees Fahrenheit'
    else:
        action = 'Hold'
    return action

# end of main.py

