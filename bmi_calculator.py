print("-------Welcome TO BMI Calculator-------")
# take weight and height from user
Weight = float(input ("Enter Your Weight in kg:"))
Height= float(input("Enter Your Height in cm:"))
if Height <= 0:
    print("Invalid height.")
else:
#convert Height from cm to m 
 Height = Height/100

 print (f"Height in m :{Height}")
 BMI= Weight/(Height**2)
 print(f"Your BMI Score is:{BMI:.2f}")
 #check BMI category
 if BMI<17.5:
   print("Underweight.")
 elif 17.5 <= BMI <=25.7:
   print ("Healthy/Normal BMI Score.")
 elif BMI<=29.9:
   print("Overweight.")
 else:
   print("Obese.")