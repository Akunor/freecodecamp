# start of main.py

def is_match(fingerprint_a, fingerprint_b):
    len_a = len(fingerprint_a)
    len_b = len(fingerprint_b)
    diff_count = 0
    if len_a != len_b:
        return False
    else:
        for a, b in zip(fingerprint_a, fingerprint_b):
            if a != b:
                diff_count += 1
        
        if diff_count * 10 > len_a:
            return False
        else:
            return True

# end of main.py
