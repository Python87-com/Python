"""
 list01[
    [1,2,3,4]，
    [5,6,7,8]，
    [9,10,11,12]，
    [13,14,15,16]
 ]
  练习1：打印第二行第三个元素
  2：打印第三行每个元素
  3：打印第一行每个元素
"""
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
# 打印第二行第三个元素
print(list01[1][2])
# 打印第三行每个元素
print(list01[2])
for i in list01[2]:
    print(i, end=" ")
print()
# 打印第一 列 每个元素 1 5 9 13
# 0 0  1 0 2 0 3 0
for i in range(len(list01)):  # 0 1 2 3
    print(list01[i][0], end=" ")

