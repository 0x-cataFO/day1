height = input("Enter your height in m: ")
weight = input("Enter you weight in kg: ")

h_as_int = float(height)
w_as_int = float(weight)

bmi = int(w_as_int / (h_as_int ** 2))


if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are overweight")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are medically obese")
