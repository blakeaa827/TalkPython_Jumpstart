import csv
import os
from rerecord import Record
import statistics

def main():
    purchases: list = get_records(file_location())
    print(purchases[0].__dict__)

def file_location():
    file = 'SacramentoRealEstateTransactions2008.csv'
    file_abs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                 'data', file)
    return file_abs_path


def get_records(file_path):
    with open(file_path, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        records = [Record.create_record_from_dict(r) for r in reader]
        return records


def get_avg_sale(purchases):
    return int(statistics.mean([int(s['price']) for s in purchases]))


def get_min_sale(purchases):
    return sorted(purchases, key=lambda p: int(p['price']))[0]


def get_max_sale(purchases):
    return sorted(purchases, key=lambda p: int(p['price']))[-1]


if __name__ == '__main__':
    main()