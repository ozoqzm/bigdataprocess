name = input("Enter the name: ")
age = int(input(f"Enter the {name}'s age: "))

if age < 10:
    print(f"{name}은 0대이다")
elif age < 20:
    print(f"{name}은 10대이다")
elif age < 30:
    print(f"{name}은 20대이다")
elif age < 40:
    print(f"{name}은 30대이다")
elif age < 50:
    print(f"{name}은 40대이다")
else:
    print(f"{name}은 50대 이상이다")
