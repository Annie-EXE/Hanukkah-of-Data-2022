# Looking for a lady who heavily utilises coupons and discounts
# Related to Anita Koch - maybe same surname?

import json

def find_customers_whose_orders_are_discounted() -> list[str]: #Returns an empty list!
    """
    Attempts to find orders where the
    profit is negative
    """
    with open('./noahs-jsonl/noahs-orders.jsonl', 'r') as jsonl_file:

        customer_ids = []

        for line in jsonl_file:

            order = json.loads(line)

            total_value = 0

            for i in range(len(order["items"])):
                total_value += order["items"][i]["qty"] * order["items"][i]["unit_price"]

            if order["total"] < total_value:
                customer_ids.append(order["customerid"])

        return(customer_ids)

# I will adjust my approach to look for the individual whose orders
# are the least profitable for Noah's Market

def find_wholesale_cost_of_item(product_id: str) -> int:
    """
    Returns the wholesale cost of
    a product, given the product ID
    """
    with open('./noahs-jsonl/noahs-products.jsonl', 'r') as jsonl_file:

        for line in jsonl_file:

            product = json.loads(line)

            if product_id == product["sku"]:
                return product["wholesale_cost"]
            
            else:
                return ValueError


def find_profitability_of_order(order: dict) -> int:
    """
    Determines profit made on an order
    """
    pass

# It has dawned on me that I will need to use Pandas or I will have
# a very sad time


