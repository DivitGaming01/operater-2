height=float(input("Enter a Height"))
weight=float(input("Enter a Weight"))
bmi=weight/(height*height)
print(bmi)
if bmi<=18.4:
    print("you are under weight")
elif bmi<=24.9:
    print("you are healthy")
elif bmi<=29.9:
    print("you are over weight")
else:
    print("you are obese")