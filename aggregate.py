total = 0
count = None

while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    num = float(inp)
    total += num
    if count is None:
        count = 1
    else:
        count += 1
