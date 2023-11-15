import random

#The function name from function_A has been changed to Generate_Random_Number
def Generate_Random_Number(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

#The function name from function_B has been changed to Generate_Random_Arithmetic_Operator
def Generate_Random_Arithmetic_Operator():
    return random.choice(['+', '-', '*'])

'''
Variable names have been changed from n1,o,n2 to number1, operator,number2, 
p has been changed to message and a to answer
'''
def Arithmetic_Operations(number1, number2, operator):
    message = f"{number1} {operator} {number2}"
    if operator == '+': answer = number1 + number2
    elif operator == '-': answer = number1 - number2
    else: answer = number1 * number2
    return message,answer

def math_quiz():
    '''s has been changed to score
    and t_q to total trials'''
    
    score = 0
    '''range() function cannot take a floating point value. So, changed it to 3.'''
    total_trials = 3 

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_trials):
        '''the random.randint() function cannot take a floating point value as min or max. So, changed it to 5.'''
        n1 = Generate_Random_Number(1, 10); n2 = Generate_Random_Number(1, 5); o = Generate_Random_Arithmetic_Operator()

        PROBLEM, ANSWER = Arithmetic_Operations(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        UserAnswer = input("Your answer: ")
        try:
            UserAnswer = int(UserAnswer)
        except:
            print('You must enter a number and not blank spaces or strings as inputs!')
       
            

        if UserAnswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score/total_trials}")
if __name__ == "__main__":
    math_quiz()