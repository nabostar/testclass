class Calculator:
    def input_extr(Self):
        expr = input('수식어를 입력하세요')
        self.expr = expr

    def calculate(self):
        return eval(self.expr)

calc = Calculator()
calc.input_extr()
print('수식 결과는 {}입니다'.format(calc.calculate()))