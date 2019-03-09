# put your python code here

one = float(input())
two = float(input())
operator = input()

if operator == "+":
    print(one + two)

elif operator == "-":
    print(one - two)

elif operator == "/":
    if two == 0:
        print("Division by 0!")
    else:
        print(one / two)

elif operator == "*":
    print(one * two)

elif operator == "mod":
    if two == 0:
        print("Division by 0!")
    else:
        print(one % two)

elif operator == "pow":
    print(one ** two)

elif operator == "div":
    if two == 0:
        print("Division by 0!")
    else:
        print(one // two)
