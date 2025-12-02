def main():
    with open("data.txt", "r") as f:
        data = f.read()
    
    pairs = [p.split('-') for p in data.split(',')]
    sum = 0

    for pair in pairs:
        for number  in range(int(pair[0]), int(pair[1])+1):
            if len(str(number))%2== 0:
                split = int(len(str(number))/2)
                if str(number)[:split] == str(number)[split:]:
                    sum += number
    print(sum)



if __name__ == "__main__":
    main()




