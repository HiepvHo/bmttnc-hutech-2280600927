def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

my_d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = 'b'
result = xoa_phan_tu(my_d, key_to_delete)
if result:
    print("Đã xóa phần tử với key '{}' khỏi dictionary{}.".format(key_to_delete, my_d))
else:
    print("Không tìm thấy key '{}' trong dictionary{}.".format(key_to_delete, my_d))