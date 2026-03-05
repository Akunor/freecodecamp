# start of main.py

def smallest_gap(s):
    last = {}
    shortest = s
    for i, char in enumerate(s):
        if char in last:
            gap = s[last[char] + 1:i]
            if len(gap) < len(shortest):
                shortest = gap
            last[char] = i 
        else:
            last[char] = i
    return shortest

# end of main.py

