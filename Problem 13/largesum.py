import csv


def main():
    with open("numbers.csv", newline="") as file:
        data = file.read().splitlines()
    

    data = [int(x) for x in data]
    total = sum(data)
    
    print(total)
    print(str(total)[:10])



if __name__ == "__main__":
    main()