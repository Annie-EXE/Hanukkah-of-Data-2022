# This attempt was unsuccessful...

# She bought pastries before 5am in 2017
# Is a woman
# Pastry product codes have BKY
# Habitually buys pastries before 5

import csv

def find_order_ids_before_5am_in_2017():

    with open("./noahs-csv/noahs-orders.csv", 'r', newline='') as csvfile:

        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)

        print(type(csv_reader))

        maybe_tinder_lady_order_id = []
    
        for row in csv_reader:

            date_time = row[-3]

            time = date_time.split(" ")[1]
            hour = time.split(":")[0]
            hour = int(hour)

            date = date_time.split(" ")[0]
            year = date.split("-")[0]
            year = int(year)

            if hour < 5:
                maybe_tinder_lady_order_id.append(row[0])

        return maybe_tinder_lady_order_id


def filter_order_ids_list_for_bakery_items(order_id_list):

    with open("./noahs-csv/noahs-orders_items.csv", 'r', newline='') as csvfile:

        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)

        bakery_orders = []

        for row in csv_reader:

            if row[0] in order_id_list and "BKY" in row[1]:

                bakery_orders.append(row[0])

    print(bakery_orders)

    return bakery_orders


def get_customer_ids_from_order_ids(order_ids_list):

    with open("./noahs-csv/noahs-orders.csv", 'r', newline='') as csvfile:

        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)

        customer_ids = []

        for row in csv_reader:

            if row[0] in order_ids_list:

                customer_ids.append(row[1])

        return customer_ids


def find_customer_info_from_customer_ids(customer_id_list):

    with open("./noahs-csv/noahs-customers.csv", 'r', newline='') as csvfile:

        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)

        customer_info = []

        for row in csv_reader:

            if row[0] in customer_id_list:

                customer_info.append(row)

        return customer_info





order_id_list_2017_mornings = find_order_ids_before_5am_in_2017()
bakery_orders = filter_order_ids_list_for_bakery_items(order_id_list_2017_mornings)
customer_ids = get_customer_ids_from_order_ids(bakery_orders)
possible_people = find_customer_info_from_customer_ids(customer_ids)

# for person in possible_people:

#     print(person[1] + " " + person[-1] + " " + str(possible_people.count(person)) + "\n")