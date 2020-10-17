weight = input("Enter your weight: ")
unit = input("(K)g or (L)bs: ")

if unit.lower() == "l":
    converted_weight = float(weight) * 0.45
    print("Your weight in Kg: " + str(converted_weight))
elif unit.lower() == "k":
    converted_weight = float(weight) / 0.45
    print("Your weight in Lbs: " + str(converted_weight))
else:
    print("You must enter L/l or K/k letters.")