# Orders containing the following items (coffee and bagel):
# BKY5887
# BKY4234
# Has initials Jd

import csv


def get_customer_id_if_initials_jd() -> list[str]:
    """
    Returns customer ID for customers
    with the initials 'JD'
    """
    with open("./noahs-csv/noahs-customers.csv", 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader) 

        customer_id_list = []

        for row in csv_reader:

            name = str(row[1])

            full_name = name.split(" ")

            if full_name[0][0] == 'J' and full_name[1][0] == 'D':

                customer_id_list.append(row[0])

    return customer_id_list


def check_for_item(product_ids: list[str]) -> list[str]:
    """
    Checks whether an order contains any
    of the items (product IDs) in the
    given list
    """
    with open("./noahs-csv/noahs-orders_items.csv", 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)

        order_ids = []

        for row in csv_reader:

            if row[1] in product_ids:

                order_ids.append(str(row[0]))
        
        return order_ids


def check_if_order_had_items_from_both_given_lists(item_1_order_ids: list[str], item_2_order_ids: list[str]) -> list[str]:
    """
    Returns a filtered list of order IDs,
    containing IDs for orders with products
    from each given list
    """
    return [id for id in set(item_1_order_ids) if id in set(item_2_order_ids)]


def check_if_order_in_2017_and_customer_in_list(order_ids: list[str], customer_id_list: list[str]) -> list[str]:
    """
    Filters a list of order IDs to contain
    only order IDs where the customer ID is in
    the given customer list, and the order
    happened in 2017
    """
    with open("./noahs-csv/noahs-orders.csv", 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)

        maybe_contractor = []
    
        for row in csv_reader:

            if row[1] in customer_id_list and row[0] in order_ids and row[3].split("-")[0] == '2017':

                maybe_contractor.append(row[1])

        return set(maybe_contractor)

            
def get_possible_contractors_names_and_numbers(customer_id_list: list[str]) -> list[tuple]:
    """
    Takes a list of customer IDs and returns
    each customer's name and phone number
    """
    with open("./noahs-csv/noahs-customers.csv", 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)

        name_list = []

        for row in csv_reader:

            if row[0] in customer_id_list:

                name_num = (row[1], row[-1])
                name_list.append(name_num)
            
        return name_list
    

if __name__ == "__main__":

    jd_name_customer_ids = get_customer_id_if_initials_jd()

    bagel_order_ids = check_for_item(['BKY5887','BKY4234'])

    coffee_order_ids = check_for_item(['DLI1464'])

    order_ids = check_if_order_had_items_from_both_given_lists(bagel_order_ids, coffee_order_ids)

    customer_id_list = check_if_order_in_2017_and_customer_in_list(order_ids, jd_name_customer_ids)

    result = get_possible_contractors_names_and_numbers(customer_id_list)

    print(result) # Returns name and number of the contractor