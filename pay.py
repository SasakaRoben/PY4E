def compute_pay(hours, rate):
    if hours > 40:
        extra_hours = hours - 40
        pay = (40 * rate) + (extra_hours * rate * 1.5)
    else:
        pay = hours * rate
    return pay

try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate Per Hour: "))

    pay = compute_pay(hours, rate)
    print("Gross Pay:", pay)
except:
    print("Error, please enter numeric input")