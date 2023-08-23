# Find lady who buys food for senior cats and lives in Queens Village

import json

def find_product_ids_from_keyword(keyword: str) -> list[str]:
    """
    Returns a list of strings of product IDs,
    for products which contain the given keyword
    in their description
    """
    with open('./noahs-jsonl/noahs-products.jsonl', 'r') as jsonl_file:

        product_ids = []

        for line in jsonl_file:

            product = json.loads(line)

            if keyword in product["desc"]:
                product_ids.append(product["sku"])
        
        return product_ids
    

def find_customers_whose_orders_include_products_from_a_list_of_product_ids(product_id_list):
    """
    Returns a list of customer IDs, for
    customers who have placed orders containing
    an item from a list of product IDs
    """
    with open('./noahs-jsonl/noahs-orders.jsonl', 'r') as jsonl_file:

        customer_ids = []

        for line in jsonl_file:

            order = json.loads(line)

            for i in range(len(order["items"])):
                product_id = order["items"][i]["sku"]
                if product_id in product_id_list:
                    customer_ids.append(order["customerid"])

        return customer_ids
    

def filter_for_customers_from_given_citystatezip(location: str, customer_ids: list):
    """
    Given a list of customer IDs, returns a
    filtered list, containing those customers
    who live in a certain location
    """
    with open('./noahs-jsonl/noahs-customers.jsonl', 'r') as jsonl_file:

        customers = []

        for line in jsonl_file:

            customer = json.loads(line)

            if (location in customer["citystatezip"]) and (customer["customerid"] in customer_ids):
                customers.append(customer["customerid"])

        return customers


def find_customers_from_customer_ids(customer_ids: list[str]) -> list[dict]:
    """
    Gets a list of customers
    (and their info) from 
    a list of customer ids
    """
    with open('./noahs-jsonl/noahs-customers.jsonl', 'r') as jsonl_file:

        possible_customers = []

        for line in jsonl_file:

            customer = json.loads(line)
            customer_id = customer["customerid"]

            if customer_id in customer_ids:
                frequency = customer_ids.count(customer_id)
                customer["freq"] = frequency
                possible_customers.append(customer)

        return possible_customers
    

if __name__ == "__main__":

    senior_cat_product_ids = find_product_ids_from_keyword("Senior Cat")
    jersey_product_ids = find_product_ids_from_keyword("Jersey")

    possible_customer_ids = find_customers_whose_orders_include_products_from_a_list_of_product_ids(senior_cat_product_ids)
    filtered_customer_ids = filter_for_customers_from_given_citystatezip("Queens Village", possible_customer_ids)
    possible_customers = find_customers_from_customer_ids(filtered_customer_ids)

    possible_customers = sorted(possible_customers, key=lambda x: x["freq"], reverse=True)

    for customer in possible_customers:
        print(customer) #Answer is the only lady from the printed list