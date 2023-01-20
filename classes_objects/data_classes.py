from dataclasses import dataclass, field, asdict
import datetime
import os
import json
import re


@dataclass()
class Employee:
    """Data container for creating employee"""
    id_num: int
    first_name: str
    middle_ini: str
    last_name: str
    age: int
    address: str
    hobbies: str = field(default='None')
    birth_date: str = datetime.date

    def __repr__(self):
        return f'Employee Data Class Contains {vars(Employee)}'


class ConfigureJson(Employee):
    """Manipulating JSON file objects"""
    info = ['id_num', 'first name', 'middle initial', 'last name', 'age',
            'address', 'hobbies']

    def __init__(self, file):
        self.path_to_file = file

    def create_json_file(self, data):
        with open(self.path_to_file, 'w') as json_f:
            json.dump(data, json_f)

    def add_entry(self):
        if not os.path.exists(self.path_to_file):
            return 'File not found'

        # Input employee data
        emp_data = [input(f'{i}: ') for i in ConfigureJson.info]

        # Prompt validator for inputting birthdate format
        while True:
            birth_date: str = input('Seperated by "-"\nEnter Birth Date: ')
            is_valid_date = re.match(r'(\d{2})[/.-](\d{2})[/.-](\d{4})$', birth_date)
            if is_valid_date:
                break
            else:
                print('Invalid format\nPlease follow input format [mm-dd-yyyy] ')
        emp_data.append(str(birth_date))
        emp = Employee(*emp_data)

        # Get previous json data
        with open(self.path_to_file, 'r') as json_f:
            loaded_data = json.load(json_f)
            loaded_data.append(asdict(emp))

        print(loaded_data)

        # Stringify
        json_data = json.dumps(loaded_data, indent=2)

        # Create json file
        with open(self.path_to_file, 'w') as json_f:
            json_f.write(json_data)

    def delete_last_entry(self):
        if not os.path.exists(self.path_to_file):
            print('File not found')

        with open(self.path_to_file, 'r') as json_f:
            loaded_data: list[dict] = json.load(json_f)
            loaded_data.pop(len(loaded_data)-1)

        json_str = json.dumps(loaded_data, indent=2)
        with open(self.path_to_file, 'w') as json_f:
            json_f.write(json_str)

    def delete_entry(self, key: str):
        if not os.path.exists(self.path_to_file):
            print('File not found')

        with open(self.path_to_file, 'r') as json_f:
            loaded_data: list[dict] = json.load(json_f)

            for idx, emp_data in enumerate(loaded_data):
                data_val = list(emp_data.values())
                for k in data_val:
                    if k == key:
                        loaded_data.pop(idx)

        json_str = json.dumps(loaded_data, indent=2)

        with open(self.path_to_file, 'w') as json_f:
            json_f.write(json_str)


def main():
    init_data = [{}]

    # path = 'data_dir/sample.json'
    # emp = ConfigureJson(path)
    # emp.delete_entry('19778')


if __name__ == '__main__':
    main()
