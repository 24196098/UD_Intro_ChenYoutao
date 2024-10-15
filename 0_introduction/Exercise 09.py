christmas_tree_height = input("please set a height of the christmas tree:")
a = int(christmas_tree_height)
for i in range(a+1):
    print (" " * (a-i) + "*" * (2*i-1))
print (" " * (a-1) + "|")