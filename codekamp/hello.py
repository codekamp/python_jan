def make_incrementer(n):
    """returns an blahfdafdaf"""

    def incrementer(x):
        return x + n

    return incrementer(n)


def make_incrementer2(n):
    return lambda (x, y): x * y + n


a = make_incrementer(5)
b = make_incrementer(9)

print(a)
print(b)
