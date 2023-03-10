# Definition of function SalCalc with call to AddNumbers
import SimpleAdd as m


def SalCalc(basic, da):
    DaAmt = basic * da / 100
    SalAmt = m.AddNumbers(basic, DaAmt)
    return SalAmt


# Executable code of module EmpSalary calling SalCalc function
print('the name of module running = ', __name__)
b = int(input('input value for basic = '))
d = int(input('input value of DA = '))
s = SalCalc(b, d)
print('amount of salary = ', s)
