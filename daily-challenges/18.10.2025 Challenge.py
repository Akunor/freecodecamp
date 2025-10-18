# start of main.py

def sock_pairs(pairs, cycles):
    i = 1
    socks = 2 * pairs
    missing_socks = 0
    print(f'Initial Socks: {socks}')

    while i <= cycles:

        if i >= 2 and i % 2 == 0:
            socks = max(0, socks - 1)
            missing_socks += 1
        if missing_socks > 0 and i >= 3 and i % 3 == 0:
            socks += 1
            missing_socks -= 1
        if i >= 5 and i % 5 == 0:
            socks = max(0, socks - 1)
        if i >= 10 and i % 10 == 0:
            socks += 2
        print(f'Socks after Cycle {i}: {socks}')
        i += 1

    remaining_pairs = socks // 2

    return remaining_pairs

# end of main.py

