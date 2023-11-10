import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as input_f:
        reader = csv.DictReader(input_f, delimiter=',', lineterminator='\n')

        records = []

        for row in reader:
            record = {}
            for column, value in row.items():
                record[column] = value
            records.append(record)

        with open(OUTPUT_FILENAME, 'w') as output_f:
            json.dump(records, output_f, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")