pencils = int(input())
markers = int(input())
cleaning_desc = int(input())
price_discount = int(input())

pencils_price = 5.80
markers_price = 7.20
cleaning_price = 1.20

sum = (pencils * pencils_price) + (markers * markers_price) + (cleaning_desc * cleaning_price)
discount = sum * price_discount / 100
total_sum = sum - discount

print(total_sum)