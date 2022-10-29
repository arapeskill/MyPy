# 多层深度神经网络的代码：
from numpy import random, dot, exp, array


# 输入层 L0 隐藏层L1 输出层L2
#          w w w
#  0                 w
#          w w w     w
#  0
#          w w w     w
#  1                 w
#          w w w
# 输入层 16节点   个数是经验值    输出点（看需求）

# 正向推导：根据输入和权重，算出结果
def fp(input_var):
    l1 = 1 / (1 + exp(-dot(input_var, w0)))
    l2 = 1 / (1 + exp(-dot(l1, w1)))
    return l1, l2


#  校正
def bp(l1, l2, y):
    error = y - l2
    slope = l2 * (1 - l2)
    l1_delta = error * slope
    l0_slope = l1 * (1 - l1)
    l0_error = l1_delta.dot(w1.T)
    l0_delta = l0_slope * l0_error
    return l0_delta, l1_delta


# 准备数据: X是输入参数, y是正确结果   [添加][注释][Sigmoid]
#                ┏━━━━┓              ┏━━━━┓      ︻
# [0, 0, 1]      random              result      0
# [1, 1, 1]      random              result      1
# [1, 0, 1]  ╳   random  ↔    0       result      1
# [0, 1, 1]      random              result      0
#                ┗━━━━┛              ┗━━━━┛      ︼

X = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
y = array([[0, 1, 1, 0]]).T

# 设置随机的权重，随机值*2再减1是为了让随机值在-1和1之间
random.seed(1)
# w0 输入层到隐藏层的权重 3->4 的权重
# w2 隐藏层到输出层的权重 4->1 的权重
w0 = random.random((3, 4)) * 2 - 1
w1 = random.random((4, 1)) * 2 - 1
weights = random.random((3, 1)) * 2 - 1

for it in range(10000):
    # 正向推导
    l0 = X
    l1, l2 = fp(l0)
    l0_delta, l1_delta = bp(l1, l2, y)

    w1 = w1 + dot(l1.T, l1_delta)
    w0 = w0 + dot(l0.T, l0_delta)

print(fp([0, 0, 0])[1])
print("<--可能性")
