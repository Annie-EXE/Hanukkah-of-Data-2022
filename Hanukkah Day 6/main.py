import pandas as pd
from pandas import DataFrame
import json


def find_customer_from_customer_name(customer_name: str) -> dict:
    """
    Gets customer info from
    customer ID
    """
    with open('./noahs-jsonl/noahs-customers.jsonl', 'r') as jsonl_file:

        for line in jsonl_file:

            customer = json.loads(line)

            if str(customer["name"]) == customer_name:
                return customer
            
        return ValueError
                
    
def merge_data() -> DataFrame:
    """
    Merges the store's CSV 
    files into one DataFrame
    """
    customers_df = pd.read_csv('/Users/anniemahmood/Documents/Coding Problems/noahs-csv/noahs-customers.csv')
    orders_items_df = pd.read_csv('/Users/anniemahmood/Documents/Coding Problems/noahs-csv/noahs-orders_items.csv')
    orders_df = pd.read_csv('/Users/anniemahmood/Documents/Coding Problems/noahs-csv/noahs-orders.csv')
    products_df = pd.read_csv('/Users/anniemahmood/Documents/Coding Problems/noahs-csv/noahs-products.csv')

    merged_orders_customers = pd.merge(orders_df, customers_df, on='customerid', how='inner')
    merged_orders_items_customers = pd.merge(merged_orders_customers, orders_items_df, on='orderid', how='inner')
    df = pd.merge(merged_orders_items_customers, products_df, on='sku', how='inner')

    df = df.drop_duplicates()

    df = df.sort_values(by='orderid', ascending=True)

    return df


if __name__ == "__main__":

    df = merge_data()

    # Create a profit column in the DataFrame
    df['profit'] = df['qty'] * (df['total'] - df['wholesale_cost'])

    # Sort the DataFrame by the value in the profit column, with smallest profits first
    df = df.sort_values(by='profit', ascending=True)

    # Include only the 70 lowest-profit orders in the DataFrame 
    df = df.head(70)

    # Identify which name occurs most frequently in the 70-row DataFrame (i.e., the customer
    # involved in the most low-profit orders)
    most_frequent_customer_name = str(df['name'].value_counts().idxmax())

    customer_info = find_customer_from_customer_name(most_frequent_customer_name)

    print(most_frequent_customer_name)
    print(customer_info)