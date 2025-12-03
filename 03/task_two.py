def main():
    batteries = []
    with open("data.txt", "r") as f:
        for line in f.readlines():
            batteries.append(line.strip())

    print(f"Number of batteries: {len(batteries)}")
    sum = 0
    for battery in batteries:
        string_to_slice = battery
        number_as_string = ""

        for i in range(11,-1,-1):
            ret, string_to_slice = get_max_between(i, string_to_slice)
            number_as_string += ret
        sum += int(number_as_string)
    print(sum)


def get_max_between(right_cuttoff, string):
    if right_cuttoff == 0:
        reduced_list = [int(c) for c in string]
    else:
        reduced_list= [int(c) for c in string[:-right_cuttoff]]
    max_num= max(reduced_list)
    split = string.find(str(max_num))+ 1
    rest = string[split:]
    return str(max_num), rest

if __name__ == "__main__":
    main()
