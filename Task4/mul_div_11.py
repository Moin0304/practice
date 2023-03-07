from add_sub_11 import calculator_v1



class calculator_v2(calculator_v1):


    def multiplication(self,a,b):
        return a*b

    def divide(self,a,b):
        return a//b

c = calculator_v2()
print(c.addition(2,3))
print(c.divide(2,2))
print(c.subtraction(2,2))
print(c.multiplication(2,2))

     
    

    

