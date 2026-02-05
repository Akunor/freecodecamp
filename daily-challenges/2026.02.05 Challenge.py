# start of main.py

def count_change(change):
    total = 0
    for count in change:
        total += int(count)

    return f'${(total / 100):.2f}'

# end of main.py

