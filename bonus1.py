user_weight = float(input("Enter your weight: "))
user_height = float(input("Enter your height: "))
bmi = user_weight / user_height**2
print("Your bmi score is: ",bmi)

if bmi >= 25:
    print("You are overwieght you need to work out more and watch your diet.")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You are fit & healthy.")
elif bmi < 18.5 :
    print("You are underweight. Watch your health.")
