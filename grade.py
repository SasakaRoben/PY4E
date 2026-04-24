def compute_grade(score):
    
    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B" 
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

try:
    score = float(input("Enter your score between 0.0 and 1.0: "))

    if score < 0.0 or score > 1.0:
        print("Error: Score must be between 0.0 and 1.0")
    else:
        grade = compute_grade(score)
        print("Your grade is:", grade)

except:
    print("Error: Please enter a numeric value")