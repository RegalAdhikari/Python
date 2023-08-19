#Now let's insert some values
name = input("Enter your name please:")
print("So you're " + name+ ". Hello " +name + "!:)")
birth_year = input("What is your birth year?")
age = 2023 - int(birth_year) #The input is in string so we convert it into int
age = str(age) #Int is converted to string for concatination :)
print("So you're " + age + " years old. :)")