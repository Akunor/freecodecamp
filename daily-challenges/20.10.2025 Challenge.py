# start of main.py

def calculate_tips(meal_price, custom_tip):
    meal_price = float(meal_price.strip('$'))
    tip_prices = [0.15, 0.20, int(custom_tip.strip('%')) * 0.01]

    tip_list = [f'${meal_price * i:.2f}' for i in tip_prices]

    return tip_list

# end of main.py

