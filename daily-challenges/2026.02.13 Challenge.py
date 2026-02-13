# start of main.py

def get_fastest_speed(times):
    lengths = [320, 280, 350, 300, 250]
    best = 0
    best_speed = 0

    for i in range(0,5):
        speed = lengths[i] / times[i]
        
        if speed > best_speed:
            best_speed = speed
            best = i + 1
    
    return f"The luger's fastest speed was {best_speed:.2f} m/s on segment {best}."

# end of main.py

