class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)
    
    def __str__(self) -> str:
        return f"{self.real} + {self.imag}i"
    
c1 = ComplexNumber(3,2)
c2 = ComplexNumber(1,7)

result = c1 + c2
print(f"The sum of Complex number is {result}")

result = c1 * c2
print(f"The product of Complex number is {result}")