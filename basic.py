
# 매개변수에 몇 개의 인자가 들어올지 모르는 경우
def add_many(*args):    # 인자들을 싹 모아서 튜플로 만들어줌
    result = 0
    print(args)
    for i in args:
        result += i
    return result

def print_kwarg(**kwarg):
    print(kwarg)

sum = add_many(1, 2, 3, 4)  
print(sum)

print_kwarg(name="myc", age="22")

add = lambda a, b: a + b
print(add(3, 4))