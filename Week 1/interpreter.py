exp = input("Expression: ").split()
x = float(exp[0])
y = exp[1]
z= float(exp[2])

match y:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        result = x / z
    case _:
        result = "Invalid operator"
print(result)