# Анализ данных

# 30-10-2016 / 04-09-2017 (161 days)  """
import csv

with open('Bakery.csv', newline='') as File:
    reader = csv.reader(File)
    count_tea_weekday = 0
    count_tea_weekend = 0
    count_coffee_weekday = 0
    count_coffee_weekend = 0
    for row in reader:
        if row[1] == 'Tea' and row[4] == 'Weekday':
            count_tea_weekday += 1
        elif row[1] == 'Tea' and row[4] == 'Weekend':
            count_tea_weekend += 1
        elif row[1] == 'Coffee' and row[4] == 'Weekday':
            count_coffee_weekday += 1
        elif row[1] == 'Coffee' and row[4] == 'Weekend':
            count_coffee_weekend += 1

    print(
        'Tea sales on weekdays: ', round(count_tea_weekday * 100 / (count_tea_weekday + count_tea_weekend), 2), '%', '\n'
        'Weekend tea sales: ', round(count_tea_weekend * 100 / (count_tea_weekday + count_tea_weekend), 2), '%', '\n'
        'Coffee sales on weekdays: ', round(count_coffee_weekday * 100 / (count_coffee_weekday + count_coffee_weekend), 2), '%', '\n'
        'Weekend coffee sales: ', round(count_coffee_weekend * 100 / (count_coffee_weekday + count_coffee_weekend), 2), '%', '\n'
    )


with open('Bakery.csv', newline='') as File:
    reader = csv.DictReader(File)
    work_dict = {}
    goods = []

    for row in reader:
        work_dict.update(row)

        for k, v in work_dict.items():
            if k == 'Items':
                goods.append(v)

    all_goods = {}

    for element in goods:
        if all_goods.get(element, None):
            all_goods[element] += 1
        else:
            all_goods[element] = 1

    sorted_goods = sorted(all_goods.items(), key=lambda a: a[1], reverse=True)

    print('Top 15 popular products: ', sorted_goods[:15], '\n')


with open('Bakery.csv', newline='') as File:
    reader = csv.DictReader(File)
    date = {}
    nov_count = 0
    dec_count = 0
    jan_count = 0
    feb_count = 0
    mar_count = 0

    for row in reader:
        date.update(row)
        for k, v in date.items():
            if v >=  '2016-01-11 07:51:20' and v <= '2016-11-30 16:48:04':
                nov_count += 1
            if v >= '2016-01-12 08:41:55' and v <= '2016-12-31 17:36:21':
                dec_count += 1
            if v >= '2017-01-01 01:21:05' and v <= '2017-01-31 17:28:11':
                jan_count += 1
            if v >= '2017-01-02 08:37:55' and v <= '2017-02-28 17:33:07':
                feb_count += 1
            if v >= '2017-01-03 09:24:44' and v <= '2017-03-31 17:23:57':
                mar_count += 1

    all_sales = nov_count + dec_count + jan_count + feb_count + mar_count

    print(
        'Distribution for the last 5 months:', '\n'
        'november: ', round(nov_count * 100 / all_sales, 2), '%', '\n'
        'december: ', round(dec_count * 100 / all_sales, 2), '%', '\n'
        'january: ', round(jan_count * 100 / all_sales, 2), '%', '\n'
        'february: ', round(feb_count * 100 / all_sales, 2), '%', '\n'
        'march: ', round(mar_count * 100 / all_sales, 2), '%', '\n'
    )


with open('Bakery.csv', newline='') as File:
    reader = csv.DictReader(File)
    all_item = {}
    all_items_count = 0
    morning_count = 0
    afternoon_count = 0
    evening_count = 0
    night_count = 0

    for row in reader:
        all_item.update(row)

        for k, v in all_item.items():
            if k == "Items":
                all_items_count += 1
            elif v == 'Morning':
                morning_count += 1
            elif v == 'Afternoon':
                afternoon_count += 1
            elif v == 'Evening':
                evening_count += 1
            elif v == 'Night':
                night_count += 1

    print(
        'Sales for all business hours: ', all_items_count, '\n'
        'Morning sales: ', morning_count, 'or', round(morning_count * 100 / all_items_count, 2), '%', '\n'
        'Afternoon sales: ', afternoon_count, 'or', round(afternoon_count * 100 / all_items_count, 2), '%', '\n'
        'Evening sales: ', evening_count, 'or', round(evening_count * 100 / all_items_count, 2), '%', '\n'
        'Night sales: ', night_count, 'or', round(night_count * 100 / all_items_count, 2), '%', '\n'
    )
