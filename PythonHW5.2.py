a = int(input("Введите первое положительное число "))
b = int(input("Введите второе положительное число "))
def rec_sum(a, b):
    if a == 0:
        return b
    else:
        return rec_sum(a - 1, b + 1)
print(rec_sum(a, b))