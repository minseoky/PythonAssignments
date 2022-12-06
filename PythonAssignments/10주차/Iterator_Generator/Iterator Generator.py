#32194579 최민석
class MultipleOfN:
    def __init__(self,n,stop = 0):
        self.n = n
        self.stop = stop
        self.temp = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.stop:
            result = self.n
            self.n += self.temp
            return result
        else:
            raise StopIteration

def MultipleofNGen(n,stop):
    num = n
    temp = n
    while num <= stop:
        yield num
        num += temp

print('Iterator')
mul1 = MultipleOfN(2,10)
i = iter(mul1)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

print('Generator')
for n in MultipleofNGen(2,10):
    print(n)
