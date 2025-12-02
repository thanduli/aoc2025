def main():
    with open("data.txt", "r") as f:
        data = f.read()
    
    pairs = [p.split('-') for p in data.split(',')]
    sum = 0

    for pair in pairs:
        for number  in range(int(pair[0]), int(pair[1])+1):
            sum += check_number(number)
    print(sum)

def check_number(number):
    number_as_string = str(number)
    len_number = len(number_as_string)
    for i in range(len_number):
        cur = i + 1
        if cur > len_number/2:
            continue
        if len_number%cur != 0:
            continue
        else:
            # slicing case
            slices = []
            number_for_slicing = number_as_string
            while len(number_for_slicing) > 0:
                slices.append(number_for_slicing[:cur])
                number_for_slicing = number_for_slicing[cur:]
            if len(set(slices))==1:
                return number
    return 0


if __name__ == "__main__":
    main()




