chicken_menu = int(input())
fish_menu = int(input())
vegie_menu = int(input())

chicken_price = 10.35
fish_price = 12.40
vegie_price = 8.15
delivery = 2.5

price_menu = chicken_menu * chicken_price + fish_menu * fish_price + vegie_menu * vegie_price
dessert = price_menu * 0.2
total_sum = price_menu + dessert + delivery

print(f"{total_sum:.2f}")

