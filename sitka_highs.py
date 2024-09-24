import csv


def main():
    filename = './datasets/sitka_weather_07-2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
        print(header)


if __name__ == '__main__':
    main()
