# 深度神经网络的代码：
from numpy import random, dot, exp, array


# 正向推导：根据输入和权重，算出结果
def fp(input_var):
    z = dot(input_var, weights)
    return 1 / (1 + exp(-z))


#  校正
def bp(y_var, output_var):
    error = y_var - output_var
    k_slope = output_var * (1 - output_var)
    return error * k_slope


# 准备数据: X是输入参数, y是正确结果   [添加][注释][Sigmoid]
#                ┏━━━━┓              ┏━━━━┓      ︻
# [0, 0, 1]      random              result      0
# [1, 1, 1]      random              result      1
# [1, 0, 1]  ╳   random  ↔           result      1
# [0, 1, 1]      random              result      0
#                ┗━━━━┛              ┗━━━━┛      ︼

X = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
y = array([[0, 1, 1, 0]]).T

# 设置随机的权重，随机值*2再减1是为了让随机值在-1和1之间
random.seed(1)
weights = random.random((3, 1)) * 2 - 1

for it in range(10000):
    # 正向推导
    output = fp(X)
    delta = bp(y, output)

    weights = weights + dot(X.T, delta)
print(weights)

print(fp([[1, 1, 0]]))
