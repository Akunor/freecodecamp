# start of main.py

def navigate(commands):
    history = ['Home']
    current = 0

    for command in commands:
        if command.startswith('Visit'):
            history.append(command[6:])
            current += 1
        elif command == 'Back' and current > 0:
            current -= 1
        elif command == 'Forward' and current < (len(history) - 1):
            current += 1
    
    return history[current]

# end of main.py

