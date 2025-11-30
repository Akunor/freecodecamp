import os
import datetime

today = datetime.datetime.now().strftime('%Y.%m.%d')

undefined_count = 0

for file in os.listdir('./daily-challenges/'):
    if file == 'undefined.txt' and undefined_count > 0:
        print('Additional undefined.txt file(s) found in daily-challenges folder.')
        break
    
    if file == 'undefined.txt' and undefined_count == 0:
        old_path = f'./daily-challenges/{file}'
        new_path = f'./daily-challenges/{today} Challenge.py'
        os.rename(old_path, new_path)
        undefined_count += 1
        
        with open(new_path, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if line.startswith('** start of main.py **'):
                lines[i] = '# start of main.py\n'
            if line.startswith('** end of main.py **'):
                lines[i] = '# end of main.py\n'
        with open(new_path, 'w') as f:
            f.writelines(lines)

if undefined_count == 0:
    print('No undefined.txt file found in daily-challenges folder.')

