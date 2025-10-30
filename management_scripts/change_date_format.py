import os

for file in os.listdir('./daily-challenges/'):
    if file.split(" ")[0].endswith('2025'):
        old_path = f'./daily-challenges/{file}'
        new_path = f'./daily-challenges/{file.split(" ")[0].split(".")[2]}.{file.split(" ")[0].split(".")[1]}.{file.split(" ")[0].split(".")[0]} Challenge.py'
        os.rename(old_path, new_path)
