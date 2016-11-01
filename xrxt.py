import random
import sys

name_list = ["张三", "李四", "王五", "赵六", "七", "八"]
print("结果如下")
counter = 0
while counter < int(sys.argv[1]):
    counter += 1
    idx = random.randint(0, len(name_list) - 1)
    print(name_list[idx])
    del name_list[idx]
