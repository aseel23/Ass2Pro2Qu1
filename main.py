#First:Loops
#Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
new_numbers = []
for i in numbers:
    if i > 150:
        if i > 500:
            break
        continue
    if i % 5 == 0:
        new_numbers.append(i)

print(new_numbers)

################################################
#Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)
else:
    print("Done!")

################################################
#Reverse a given integer number
num = 76542
reverse_number = 0
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)
