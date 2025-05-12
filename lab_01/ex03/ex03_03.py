def tao_tuple(lst):
    return tuple(lst)

input_list = input("Nhập danh sách số (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_tuple(numbers)
print("list: ", numbers)
print("Tuple: ", my_tuple)