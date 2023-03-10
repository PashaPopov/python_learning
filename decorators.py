def NewTax(func):
    surchange = 2

    def inner(basic, tax):
        if tax > 10:
            NewPrice = func(basic, tax)
        else:
            NewPrice = func(basic, tax) + (basic * surchange / 100)
        return NewPrice

    return inner


@NewTax
def SalePrice(basic, tax):
    price = basic + (basic * tax / 100)
    return price


CurrPrice1 = SalePrice(50, 8)
print('Price for tax at rate of 8 = ', CurrPrice1)

CurrPrice2 = SalePrice(50, 20)
print('Price for tax at rate of 12 = ', CurrPrice2)

CurrPrice = NewTax(SalePrice)
print('Price for tax at rate of 8 = ', CurrPrice(50, 8))
