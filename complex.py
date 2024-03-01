class TComplex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return TComplex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return TComplex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return TComplex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )

    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return TComplex(real_part, imag_part)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __repr__(self):
        return f"TComplex({self.real}, {self.imag})"

    

