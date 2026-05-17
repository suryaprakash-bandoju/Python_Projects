import random

number = random.randint(1,100)
count = 0

while True:
    try:
        guess_num = int(input("Enter Your guess number(1 to 100): "))
        count += 1
        if guess_num > number:
            print("Too High...")
        elif guess_num < number:
            print("Too Low...")
        else:
            break
    except ValueError:
        print("Please enter a valid number!")
print(f"Correct! It took you {count} attempts.")
    