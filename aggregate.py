total = 0
count = None

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

average = total / count
