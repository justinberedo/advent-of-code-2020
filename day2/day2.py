input = open("/home/jberedo/python-projects/advent-of-code-2020/day2/day2.txt", "r")
content_list = input.readlines()
clean_list = [x.strip('\n') for x in content_list]

print(clean_list[0].split())

def count_instances(letter: str, password: str):
    count = 0
    for i in range(len(password)):
        if letter == password[i]:
            count += 1
    return count

def part1(clean_list):
    valid = 0
    for record in clean_list:
        record_values = record.split()
        numbers = record_values[0].split('-')
        min_num = int(numbers[0])
        
        max_num = int(numbers[1])
        
        letter = record_values[1].replace(':', '')
        
        password = record_values[2]
        
        num_instances = count_instances(letter, password)
        
        if (min_num <= num_instances) and (num_instances <= max_num):
            valid += 1
    return valid

def part2(clean_list):
    valid = 0
    for record in clean_list:
        record_values = record.split()
        numbers = record_values[0].split('-')
        min_num = int(numbers[0])
        
        max_num = int(numbers[1])
        
        letter = record_values[1].replace(':', '')
        
        password = record_values[2]
        
        if (password[min_num-1] == letter) and (password[max_num-1] != letter):
            valid += 1
        elif (password[min_num-1] != letter) and (password[max_num-1] == letter):
            valid += 1
        else:
            pass
    return valid

if __name__ == "__main__":
    
            
    print(part1(clean_list))
    print(part2(clean_list))