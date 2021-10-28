from tqdm import tqdm


my_file = open("/home/jberedo/python-projects/advent-of-code-2020/day1/input1.txt", "r")
content_list = my_file.readlines()
clean_list = [int(x.strip('\n')) for x in content_list]

def get_product_part_1(clean_list):
    for i in range(len(clean_list)):
        num1 = clean_list[i]
        for num2 in clean_list[i:]:
            if num1 + num2 == 2020:
                print(num1 * num2)
                return num1 * num2

def get_product_part_2(clean_list):
    len_list = len(clean_list)
    for i in range(len_list):
        num1 = clean_list[i]
        for o in range(len_list):
            if i == o:
                break
            else:
                num2 = clean_list[o]
                for p in range(len_list):
                    if (p == i) or (p == o):
                        break
                    else:
                        num3 = clean_list[p]
                        if num1 + num2 + num3 == 2020:
                            return num1 * num2 * num3


if __name__ == "__main__":
    print(get_product_part_1(clean_list))
    print(get_product_part_2(clean_list))