import csv
import os
from rerecord import Record
import statistics


def main():
    purchases: list = get_records(file_location())

    print(f"The minimum price of all houses sold was",
          f"${get_min_sale(purchases).price:,}\n")

    print(f"The maximum price of all houses sold was",
          f"${get_max_sale(purchases).price:,}\n")

    print(f"The average price of all homes were",
          f"${get_avg_sale(purchases):,}\n")

    print(f"The average price of a 2 bedroom home was",
          f"${get_avg_sale(purchases, ['beds'], [2]):,}\n")

    print(f"The average price of a 3 bathroom home was",
          f"${get_avg_sale(purchases, ['baths'], [3]):,}\n")

    print(f"The average price of a 3 bedroom home with 2 baths was",
          f"${get_avg_sale(purchases, ['beds', 'baths'], [3, 2]):,}\n")


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


def get_avg_sale(purchases, stats=list(), values=list()):
    if not stats:
        return int(statistics.mean((p.price for p in purchases)))
    elif len(stats) != len(values):
        raise ValueError('a value must be supplied for each requested stat')
    else:
        # filtered_purchases = filter_purchases(
        #     purchases, lambda x: x.__getattribute__(stat) == value
        # )
        return int(statistics.mean((p.price
                                    for p in purchases
                                    if filter_purchases(p, stats, values)
                                    )))


def filter_purchases(purchase, stats, values):
    for count, stat in enumerate(stats):
        if purchase.__getattribute__(stat) != values[count]:
            return None
        else:
            pass
    return purchase


def get_min_sale(purchases):
    return sorted(purchases, key=lambda p: p.price)[0]


def get_max_sale(purchases):
    return sorted(purchases, key=lambda p: p.price)[-1]


if __name__ == '__main__':
    main()
