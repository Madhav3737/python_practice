class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def complex_add(self,sec_no):
        real = self.real+sec_no.real
        imag = self.imag+sec_no.imag
        return Complex(real,imag)
    def __str__(self):
        return f"{self.real}+{self.imag}i"
number1=Complex(5,6)
number2=Complex(-2,3)
sum = number1.complex_add(number2)
print(sum.real,"+",sum.imag,"i")
print(sum)


