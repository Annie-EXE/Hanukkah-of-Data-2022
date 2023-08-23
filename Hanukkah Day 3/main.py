import csv
from datetime import datetime

# Aries birthdays: March 21 – April 19
# Years of the Dog: 1946, 1958, 1970, 1982, 1994, 2006, 2018

def get_customer_info_if_aries_dog() -> list[list]:
    """
    Filters a list of customers, returning
    those born in a Year of the Dog between
    March 21 and April 19
    """
    with open("./noahs-csv/noahs-customers.csv", 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader) 

        customer_list = []

        dog_birth_years = ['1946', '1958', '1970', '1982', '1994', '2006', '2018']

        for row in csv_reader:

            birthday = row[4]
            
            bday_split = birthday.split("-")

            if bday_split[1] == "03" and int(bday_split[2]) >= 21:

                valid_date = True

            elif bday_split[1] == "04" and int(bday_split[2]) <= 19:

                valid_date = True
            
            else:

                valid_date = False

            if bday_split[0] in dog_birth_years and valid_date == True:

                customer_list.append(row)
        
        return customer_list


def check_if_customer_address_contains_keyword(customer_data: list[list], keyword: str) -> list[list]:
    """
    Filters a list of customers, returning
    those whose address contains the
    provided phrase
    """
    filtered_customers = []

    for customer in customer_data:
        if keyword in customer[3]:
            filtered_customers.append(customer)

    return filtered_customers


if __name__ == "__main__":

    aries_dogs = get_customer_info_if_aries_dog()

    aries_dogs_in_area = check_if_customer_address_contains_keyword(aries_dogs, "South Ozone Park")

    print(aries_dogs_in_area)