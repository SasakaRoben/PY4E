total = 0
numbers = list()

while True:
    inp = input("Enter a number or 'done' to stop: ")
    if inp == "done":
        break

    try:
        num = float(inp)
    except:
        print("Invalid input")
        continue

    numbers.append(num)

if len(numbers) == 0:
    print("No numbers were entered.")
    exit()
average = sum(numbers) / len(numbers)
print("Count:", len(numbers))
print("Total:", sum(numbers))
print("Average:", average)
print("Largest:", max(numbers))
print("Smallest:", min(numbers))
