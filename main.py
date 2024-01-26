import os
import re
from datetime import datetime


def main():
    directory = '/home/admin/Python/add_date/migrations/'

    files = os.listdir(directory)

    begin_str = r'\d{4}_\d\d_\d\d_\d{4}-.'

    a = 'Create Date:'

    for file in files:
        valid = re.match(begin_str, file)
        if valid:
            continue

        with open(directory + file, 'r+') as f:
            for line in f:
                if a in line:
                    split_str = line.split()
                    full_date = split_str[2] + ' ' + split_str[3]
                    datetime_obj = datetime.strptime(full_date, '%Y-%m-%d %H:%M:%S.%f')
                    formated_date = datetime_obj.strftime('%Y_%m_%d_%H%M-')
                    new_name = f'{formated_date}{file}'
                    os.rename(directory + file, directory + new_name)
                    break


if __name__ == '__main__':
    main()
