useroperation_list = []
userdata_list = []
num_operations = int(input())
for i in range(num_operations):
    a = input()
    useroperation_list.append(a)
for operation in useroperation_list:
    parts = operation.split()
    num = parts[0]
    if num == "insert":
        index, value = int(parts[1]), int(parts[2])
        userdata_list.insert(index, value)
    elif num == "append":
        value = int(parts[1])
        userdata_list.append(value)
    elif num == "remove":
        value = int(parts[1])
        if value in userdata_list:
            userdata_list.remove(value)
        else:
            print(value)
    elif num == "reverse":
        userdata_list.reverse()
    elif num == "sort":
        userdata_list.sort()
        print(userdata_list)
    elif num == "print":
        print(userdata_list)