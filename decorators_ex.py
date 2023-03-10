def NewTax(func):
    imp = 10

    def inner(basic, tax):
        if basic < 5000:
            NewPrice = func(basic, tax) + (basic * imp/100)
        else:
            NewPrice = func(basic, tax)
        return NewPrice

    return inner


@NewTax
def Salary(basic, tax):
    price = basic + (basic * tax / 100)
    return price


CurrSall = Salary(6000, 10)
print('Salary of 6000 = ', CurrSall)

CurrSall1 = Salary(4000, 10)
print('Salary of 5000 = ', CurrSall1)

