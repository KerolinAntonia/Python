def conta(num1,num2,s):
    if s == "+":
        r = num1 + num2
        return r
    if s == "-":
        r = num1 - num2
        return r
    if s == "*":
        r = num1 * num2
        return r
    if s == "/":
        r = num1 / num2
        return r
    
print(conta((int(input("Número: "))),(int(input("Número: "))),(input("Conta: "))))
    
    
    
    