def main():
    batteries = []
    with open("data.txt", "r") as f:
        for line in f.readlines():
            batteries.append(line.strip())

    print(f"Number of batteries: {len(batteries)}")
    sum = 0
    for battery in batteries:
        max_Num = max([int(c) for c in battery[:-1]])
        split = battery.find(str(max_Num))+ 1
        second_max = max([int(c) for c in battery[split:]])
        number = int(str(max_Num)+str(second_max))
        sum += number
    print(sum)



if __name__ == "__main__":
    main()
