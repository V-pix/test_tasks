from collections import OrderedDict


def name_file(names: list):
    unique_names: list = []
    for i in names:
        unique_name = "".join(OrderedDict.fromkeys(i))
        unique_names.append(unique_name)
    max_name = max(unique_names, key=len)
    count = len(max_name)
    new_names: list = []
    for i in unique_names:
        add = count - len(i)
        new_name = i + "_" * add
        new_names.append(new_name)
    return new_names


if __name__ == "__main__":
    names = ["f", "dfgr", "wecdwfdv", "sdvdvss"]
    print(name_file(names))
