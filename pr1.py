# personal data collector

print("welcome to the intractive data collector,we are so excited for collect your information")
Name=input("please sign your name")
Age=int(input("Please enter your age"))
Height=float(input("Please enter your height in meters"))
Fav_number=int(input("please enter your fav_number"))
print(f"Name:{Name} age:{Age},height:{Height},fav_number:{Fav_number},\n we appreciated!for give us your information thank you!\U0001F600")
print(F"Name:{Name}(type:{type(Name)}, memory address:{id(Name)}")
print(f"Age:{Age}(type:{type (Age)}, memory address:{id(Age)}")
print(f"Height:{Height}(type:{type(Height)}, memory address:{id(Height)}")
print(f"Fav_number:{Fav_number}(type:{type(Fav_number)}, memory address:{id(Fav_number)}")

#calculate approximate birth year=
current_year=2026
birth_year = current_year - Age
print(f"\nYour birth year is approximately:{birth_year}(according to your age of{Age})")

print("\nThank you for using the personal data collector.goodbye!have a nice day\U0001F600")
