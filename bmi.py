weight = input("体重は？")
height = input("身長は？")
bmi = float(weight) / (float(height) / 100) ** 2
print("BMIは", bmi)
if bmi < 18.5:
    print("痩せ型")
elif bmi > 25:
    print("肥満")
else:
    print("普通")