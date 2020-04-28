# https://stepik.org/lesson/25969/step/5?unit=196192
import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
print(fun(5))