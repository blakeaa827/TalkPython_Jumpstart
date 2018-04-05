import csv
import os

def main():
    file = 'SacramentoRealEstateTransactions2008.csv'
    file_abs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                 'data', file)
    purchases = get_records(file_abs_path)

    for p in purchases:
        print(p)


def get_records(archive):
    with open(archive, 'r', encoding='utf-8') as fin:
        readCSV = csv.DictReader(fin)
        records = [p for p in readCSV]
    return records


if __name__ == '__main__':
    main()