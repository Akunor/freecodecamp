# start of main.py

def send_message(route):
    satellites = len(route)-1
    time = satellites*0.5

    for dis in route:
        time += dis/300000

    time = round(time, 4)
    
    return time

# end of main.py

