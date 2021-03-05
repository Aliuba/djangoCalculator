from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'calculator/home.html')


def calc(reguest, numberOne, calc, numberTwo ):
    if calc == '+':
        s = numberOne+numberTwo
        print(numberOne, numberTwo)
        return render(reguest, 'calculator/calc.html', {'numberOne': numberOne, 's': s, 'numbertwo': numberTwo})
    if calc == 'div':
        div = numberOne / numberTwo
        print(numberOne, numberTwo)
        return render(reguest, 'calculator/calc.html', {'numberOne': numberOne, 'div': div, 'numbertwo': numberTwo})
    if calc == '-':
        sub = numberOne - numberTwo
        print(numberOne, numberTwo)
        return render(reguest, 'calculator/calc.html', {'numberOne': numberOne, 'sub': sub, 'numbertwo': numberTwo})
    if calc == '*':
        mult = numberOne * numberTwo
        print(numberOne, numberTwo)
        return render(reguest, 'calculator/calc.html', {'numberOne': numberOne, 'mult': mult, 'numbertwo': numberTwo})
    return render(reguest, 'calculator/calc.html')


