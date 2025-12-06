def read_input(file_path):
    with open(file_path) as f:
        data = f.read().strip()
    return data

def main():
    input = read_input('data.txt')
    input_part_one, input_part_two = input.split('\n\n')
    ranges = [(int(i.split('-')[0]), int(i.split('-')[1])) for i in input_part_one.split('\n')]
    print(f"count range {len(ranges)}")
    to_be_checked = [int(i) for i in input_part_two.split('\n')]
    print(len(to_be_checked))
    sum = 0
    for n in to_be_checked:
        if check_number(n, ranges) == True:
            sum += 1



    print(sum)


def check_number(number, ranges):
    for r in ranges:
        if check_range(number,r)==True:
            return True
    return False

        

def check_range(number, values):
    if number >= values[0] and number <= values[1]:
        return True
    else:
        return False
        
    


if __name__== "__main__":
    main()
