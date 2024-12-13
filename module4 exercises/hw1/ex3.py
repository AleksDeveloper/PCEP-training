def evaluate_bmi(weight, height):
    bmi = weight / (height**2)
    if bmi < 18.5: return f"{bmi}: You are underweight"
    if 18.5 <= bmi < 24.9: return f"{bmi}: You are normal weight"
    if 25 <= bmi < 29.9: return f"{bmi}: You are normal weight"
    if bmi >= 30: return f"{bmi}: You are in obesity"

def main():
    print(evaluate_bmi(84.5, 1.80))
    print(evaluate_bmi(120, 1.80))
    print(evaluate_bmi(59, 1.58))
    
main()
