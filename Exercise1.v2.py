# 2. FUNCTION CHECKS FOR NUMBERS THAT CAN BE DIVIDED BY 3 AND 5, AND SUM THEM
def sum_func(n):
    sum_result = 0
    for i in range(1, n + 1):
        if i >= 1 and i % 3 == 0 or i % 5 == 0:
            sum_result += + i
        else:
            pass
    return sum_result


# 1. VALIDATING USERS INPUT AND IF VALID, RUNS THE FUNCTION
try:
    user_input = int(input("Write an integer number greater than 0 here:"))
    if isinstance(user_input, int):
        if user_input < 1:
            print(f' You entered the number {user_input}. Please enter a higher number.')
        else:
            print(f'{user_input} is a valid number.')
            n = user_input
            print(sum_func(n))
    else:
        pass
except ValueError:
    print("This is not a valid number. Please try again.")
