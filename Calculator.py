class Calculator:
    def addition(self,x,y):
        return x + y
    def subtraction(self,x,y):
        return x - y
    def multiplication(self,x,y):
        return x * y
    def division(self,x,y):
        if y == 0:
            return "Error: Division by zero is not allowed."
        else:
            return x / y
cal=Calculator()
a,b=map(int,input("Enter 2 numbers to calculate : ").split())
print("Addition (",a,"+",b,"):",cal.addition(a,b))
print("Subtraction (",a,"-",b,"):",cal.subtraction(a,b))
print("Multiplication (",a,"*",b,"):",cal.multiplication(a,b))
print("Division (",a,"/",b,"):",cal.division(a,b))