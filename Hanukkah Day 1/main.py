import csv

def read_csv():
    with open("./noahs-csv/noahs-customers.csv", 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader) 

        data_list = []

        for row in csv_reader:
            name = row[1]
            surname = name.split(" ")[-1]
            phone_number = row[-1]

            data = {'name': surname, 'number': phone_number}
            data_list.append(data)

    return data_list


number_letter_dict = {'2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}


def check_if_number_is_name(data_list):
    for person in data_list:
        number = person['number'].replace("-", "")
        name_number = ''

        for char in list(person["name"].upper()):
            for key, value in number_letter_dict.items():
                if char in value:
                    name_number += key

        print(person['name'])
        print("name as number:" + name_number)
        print("phone number:" + number)

        if name_number == number:
            return number


print(read_csv())
print(check_if_number_is_name(read_csv()))

def read_csv_full_names():
    with open("./noahs-csv/noahs-customers.csv", 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader) 

        data_list = []

        for row in csv_reader:
            name = row[1]
            data_list.append(name)

        return data_list

def check_initials(data_list: list):

    full_names_split = []

    for name in list:

        full_name_split = name.split(" ")

        full_names_split.append(full_name_split)

    print(full_names_split)


