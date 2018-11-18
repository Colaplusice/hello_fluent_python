def gen():
    for i in "AB":
        yield i

    for i in range(18):
        yield i


a = list(gen())
print(a)


def gen_yield_from(*iterbles):
    for it in iterbles:
        yield from it


a = "abc"

b = [1, 2, 3]

result = gen_yield_from(a, b)

print(list(result))
