product = input()
day_of_week = input()
quantity = float(input())
condition = True

if day_of_week in 'Monday' 'Tuesday' 'Wednesday' 'Thursday' 'Friday':
    if product == 'banana':
        price = 2.50
    elif product == 'apple':
        price = 1.20
    elif product == 'orange':
        price = 0.85
    elif product == 'grapefruit':
        price = 1.45
    elif product == 'kiwi':
        price = 2.70
    elif product == 'pineapple':
        price = 5.50
    elif product == 'grapes':
        price = 3.85
    else:
        condition = False

elif day_of_week in 'Saturday' 'Sunday':
    if product == 'banana':
        price = 2.70
    elif product == 'apple':
        price = 1.25
    elif product == 'orange':
        price = 0.90
    elif product == 'grapefruit':
        price = 1.60
    elif product == 'kiwi':
        price = 3.00
    elif product == 'pineapple':
        price = 5.60
    elif product == 'grapes':
        price = 4.20
    else:
        condition = False

sum = price * quantity
if condition:
    print(f'{sum:.2f}')
else:
    print('error')



