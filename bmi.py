def calculate_bmi(height,weight):
    print("Heignht = ",height)
    print("Weight = ",weight)
    BMI = weight/(height**2)
    print("BMI = ",round(BMI,2))
    #round(var, number) is to round the number to that number
    print("Weight Classification: ", end="")
    if BMI < 18.5:
        print("Underweight")
        return -1
    elif BMI >25.0:
        print("Overweight")
        return 1
    else:
        print("Normal weight")
        return 0


result = calculate_bmi(weight =57, height = 1.75)
print("result : ", result)
print("==========================")
result = calculate_bmi(weight =80, height = 1.75)
print("result : ", result)
print("==========================")
result = calculate_bmi(weight =47, height = 1.75)
print("result : ", result)

