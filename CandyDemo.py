# class Candy:
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color

class Candy:
    def __init__(self, shape, color):   # 던더__ 라고 부름
        self.shape = shape
        self.color = color



# satang = Candy()
# satang.set_info('circle','brown')

satang = Candy('circle','brown')

print(satang.shape)
print(satang.color)

class Sample:
    def __del__(self):
        print('has been closed')

sample = Sample()
del sample
