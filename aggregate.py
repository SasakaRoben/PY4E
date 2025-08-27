total = 0
count = None
largest = None
smallest = None

while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break

    try:
        num = float(inp)
    except:
        print("Invalid input")
        continue

    total += num

    if count is None:
        count = 1
    else:
        count += 1
    
    if largest is None or num > largest:
        largest = num
    
    if smallest is None or num < smallest:
        smallest = num

average = total / count
print("Count:", count)
print("Total:", total)
print("Average:", average)
