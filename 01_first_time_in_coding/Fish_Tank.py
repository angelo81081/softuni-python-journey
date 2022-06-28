lenght = int(input())
width = int(input())
hight = int(input())
percentage = float(input())

volume_tank = lenght * width * hight
volume_water_cm = volume_tank - volume_tank * percentage / 100
volume_water_dm = volume_water_cm / 1000

print(volume_water_dm)
