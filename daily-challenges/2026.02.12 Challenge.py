# start of main.py

def largest_difference(skater1, skater2):
    largest_gap = 0
    gap_lap_num = 0

    for i in range(0, len(skater1)):
        diff = abs(skater1[i] - skater2[i])

        if diff > largest_gap:
            largest_gap = diff
            gap_lap_num = i + 1

    return gap_lap_num

# end of main.py

