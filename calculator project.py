# calculator project
import calculator_art
print(calculator_art.logo)

# todo1-write out the outer 3 functions -subtract,multiply and divide.
 
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

# todo 2- Add these 4 functions into a dictionary as the value.keys="+","-","*","/"
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
# todo3- use the dictionary to perform the calculations.miltiply 4 + 8 using the dictionary.
# print(operations["*"](4,8))  ----> 32

def calculator():    
    should_accumulate=True
    num1=float(input("What is the first number?: "))
    while should_accumulate:
        for symbol  in operations:
            print(symbol)
        operation_symbol=input("Pick an operation: ")    
        num2 = float(input("What's the second number?\n>> "))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice=input(f"Type 'y' to continue calculating with {answer}, or type 'n' if you want to start new calculation!\n>>")
        if choice =='y':
            num1 = answer
        else:  
            should_accumulate = False
            print("\n" *20)  
            calculator()


calculator()