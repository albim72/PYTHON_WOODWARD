#przykład 1
def liczby():
    for i in range(27):
        yield i*3


print(liczby())
print(list(liczby()))

for p in liczby():
    print(p)

#przykład 2

def wstrzymanie(n,k):
    print("wstrzymanie działania 0")
    yield 1001
    print("wznowienie działania 1")
    yield n+k
    print("wstrzymanie działania 1")
    yield n-k
    print("wznowienie działania 2")
    print("wstrzymanie działania 2")
    n = 8*k-200
    yield n*k
    print("wznowienie działania 3")
    print("wstrzymanie działania 3")
    yield n/k
    print("wznowienie działania 4")
    print("wstrzymanie działania 4")
    yield n%k
    print("wznowienie działania 5")

print(wstrzymanie(7,8))
print("_"*60)

print(tuple(wstrzymanie(7,8)))
for i in wstrzymanie(7,8):
    print("*"*50)
    print(type(i))
    print(f"zwróconow wartość: {i}")

