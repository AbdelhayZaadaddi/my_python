class Emplayee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def Fullname(self):
        return '{} {}'.format(self.first, self.last)
    def Email(self):
        return self.email
emp_1 = Emplayee('Abdelhay', 'Zaadaddi', 11000)
emp_2 = Emplayee('lhay', 'daddi', 11000)

