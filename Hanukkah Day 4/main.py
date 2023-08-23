# Woman who habitually buys pastries before 5

import json


def find_customers_who_order_multiple_pastries_before_5am() -> list[str]:
    """
    Identifies customer ids of customers who 
    placed orders between midnight and 5am
    """
    with open('./noahs-jsonl/noahs-orders.jsonl', 'r') as jsonl_file:

        maybe_tinder_lady_customer_id = []

        for line in jsonl_file:

            order = json.loads(line)

            date_time = order["ordered"]

            time = date_time.split(" ")[1]
            hour = time.split(":")[0]
            hour = int(hour)

            bakery_items_count = 0
            for i in range(len(order["items"])):
                if "BKY" in order["items"][i]["sku"]:
                    bakery_items_count += 1 * int(order["items"][i]["qty"])

            if hour < 5 and bakery_items_count > 1:
                maybe_tinder_lady_customer_id.append(order["customerid"])

        return maybe_tinder_lady_customer_id
    

def find_customers_from_customer_ids(customer_ids: list[str]) -> list[dict]:
    """
    Gets a list of customers from 
    a list of customer ids
    """
    with open('./noahs-jsonl/noahs-customers.jsonl', 'r') as jsonl_file:

        maybe_tinder_lady_info = []

        for line in jsonl_file:

            customer = json.loads(line)
            customer_id = customer["customerid"]

            if customer_id in customer_ids:
                frequency = customer_ids.count(customer_id)
                customer["freq"] = frequency
                maybe_tinder_lady_info.append(customer)

        return maybe_tinder_lady_info


if __name__ == "__main__":

    possible_customer_ids = find_customers_who_order_multiple_pastries_before_5am()
    possible_customers = find_customers_from_customer_ids(possible_customer_ids)
    possible_customers = sorted(possible_customers, key=lambda x: x["freq"], reverse=True)

    for customer in possible_customers:
        # First customer to be printed is the one who most habitually 
        # purchases pastries early morning
        print(customer)