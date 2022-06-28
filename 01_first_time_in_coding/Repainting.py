nylon = float(input())
paint = float(input())
diluent  = float(input())
hour_work = int(input())

price_nylon = 1.5
price_paint = 14.5
price_diluent = 5.00
price_bag = 0.40

sum_nylon = nylon * price_nylon + 2 * price_nylon
sum_paint = paint * price_paint + (paint * price_paint) * 0.1
sum_diluent = diluent * price_diluent
sum_work = ((sum_nylon + sum_diluent + sum_paint + price_bag) * 0.3) * hour_work
total_sum = sum_nylon + sum_diluent + sum_paint + price_bag + sum_work

print(total_sum)
