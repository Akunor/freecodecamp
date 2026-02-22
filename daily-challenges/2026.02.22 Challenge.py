# start of main.py

class country:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.silver = 0
        self.bronze = 0
        self.total = 0

    def add_medal(self, position):
        if position == 0:
            self.gold += 1
            self.total += 1
        elif position == 1:
            self.silver += 1
            self.total += 1
        elif position == 2:
            self.bronze += 1
            self.total += 1

def count_medals(winners):
    country_list = []
    countries = []

    for event in winners:
        for i in [0, 1, 2]:
            if event[i] not in country_list:
                country_list.append(event[i])
                countries.append(country(event[i]))
                countries[country_list.index(event[i])].add_medal(i)
            else:
                countries[country_list.index(event[i])].add_medal(i)
    
    countries.sort(key=lambda x: (-x.gold, x.name))

    medal_table = "Country,Gold,Silver,Bronze,Total"

    for i in range(0,len(countries)):
        medal_table += f"\n{countries[i].name},{countries[i].gold},{countries[i].silver},{countries[i].bronze},{countries[i].total}"

    return medal_table

# end of main.py

