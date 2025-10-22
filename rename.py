import os
import datetime

today = datetime.datetime.now().strftime('%d.%m.%Y')



for file in os.listdir('./daily-challenges/'):
    if file == 'undefined.txt':
        old_path = f'./daily-challenges/{file}'
        new_path = f'./daily-challenges/{today} Challenge.py'
        os.rename(old_path, new_path)

    # insert code here to replace the incorrect comment markings before 'start of main.py' and before 'end of main.py' with #'s
        with open(new_path, 'r') as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            if line.startswith('** start of main.py **'):
                lines[i] = '# start of main.py\n'
            if line.startswith('** end of main.py **'):
                lines[i] = '# end of main.py\n'
        with open(new_path, 'w') as f:
            f.writelines(lines)
