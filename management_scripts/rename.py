import os
import datetime

today_date = datetime.datetime.now()
today = today_date.strftime('%Y.%m.%d')

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

response =input('Is the file ready to be pushed? (y/n)')
if response == 'y':
    print('Pushing file to GitHub...')
    os.system('git add .')
    os.system(f'git commit -m "Daily Challenge {today_date.strftime("%-d")}{"st" if today_date.day in [1, 21, 31] else "nd" if today_date.day in [2, 22] else "rd" if today_date.day in [3, 23] else "th"} of {today_date.strftime("%B")} {today_date.year}"')
    os.system('git push origin main')
    print('File pushed to GitHub.')
else:
    print('File not pushed to GitHub.')

