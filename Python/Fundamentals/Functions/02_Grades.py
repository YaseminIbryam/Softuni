def grading(grade):
    if 2 <= grade < 3:
        return "Fail"
    elif grade < 3.50:
        return "Poor"
    elif grade < 4.50:
        return "Good"
    elif grade < 5.50:
        return "Very Good"
    elif grade <= 6:
        return "Excellent"


grade = float(input())
print(grading(grade))
