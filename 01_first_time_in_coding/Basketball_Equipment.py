annual_subscription = float(input())

shoes_price = annual_subscription * 0.6
dress_price = shoes_price * 0.8
ball_price = dress_price * 0.25
accesories_price = ball_price * 0.2

total_sum = annual_subscription + shoes_price + dress_price + ball_price + accesories_price
print(total_sum)