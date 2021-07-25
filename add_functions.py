import csv
import os.path
from datetime import datetime
import employee_class
import json

employee_json = 'Employees.json'
time_logs_json = 'TimeLogs.json'

id_is_valid = lambda value: value.isdecimal() and len(value) == 4
full_name_is_valid = lambda value: ''.join(value.split()).isalpha() and len(value.split()) > 1
phone_number_is_valid = lambda value: ''.join(value.split('-')).isdecimal() and len(''.join(value.split('-'))) == 10
age_is_valid = lambda value: value.isdecimal() and 18 <= int(value) <= 67


def enter_id():
    correct = False
    while not correct:
        employee_id = input('Employee ID (numbers, 4 digits): ')
        if id_is_valid(employee_id):
            correct = True
        else:
            print('Wrong ID, try again')
    return employee_id


def enter_full_name():
    correct = False
    while not correct:
        full_name = input('Employee Full Name: ')
        if full_name_is_valid(full_name):
            correct = True
        else:
            print('Please enter Full Name (First name and Second name)')
    return full_name


def enter_phone_number():
    correct = False
    while not correct:
        phone_number = input('Employee Phone Number: ')
        if phone_number_is_valid(phone_number):
            correct = True
        else:
            print('Wrong Number, try again')
    return phone_number


def enter_age():
    correct = False
    while not correct:
        age = input('Employee Age (18-67): ')
        if age_is_valid(age):
            correct = True
        else:
            print('Wrong Age, try again')
    return age


def enter_employee_details():
    employee_id = enter_id()
    full_name = enter_full_name()
    phone_number = enter_phone_number()
    age = enter_age()
    return employee_id, full_name, phone_number, age


def check_file_exists(file):
    file_exist = os.path.isfile(file)
    if not file_exist:
        print("File doesn't exist")
    return file_exist


def enter_file_path():
    correct = False
    while not correct:
        file_path = input('Enter file path: ')
        file_exist = check_file_exists(file_path)
        if not file_exist:
            continue
        file_path_ext = file_path[len(file_path) - 3:]
        if file_path_ext != 'csv':
            print("It must be csv file")
            continue
        correct = True
    return file_path


get_employee_by_id = lambda employee_id, employees_list: next(
    (row for row in employees_list if row['id'] == employee_id), None)


def get_items_list_from_json_file(file):
    items_list = []
    try:
        with open(file, 'r') as f:
            json_content = f.read()
            items_list_json = json.loads(json_content)
            if type(items_list_json) == list:
                items_list = items_list_json
    except:
        pass
    return items_list


def update_file_json(employees_list, file):
    employees_content = json.dumps(employees_list, indent=4)
    with open(file, 'w') as f:
        f.write(employees_content)


def add_employee_to_file(employee_id, full_name, phone_number, age):
    employees_list = get_items_list_from_json_file(employee_json)
    employee = get_employee_by_id(employee_id, employees_list)
    if employee:
        print('Employee with ID {} is already in the list'.format(employee_id))
    else:
        new_employee = employee_class.Employee(employee_id, full_name, phone_number, age)
        employees_list.append(new_employee.get_employee())
        try:
            update_file_json(employees_list, employee_json)
            print('Employee added: ', employee_id, full_name, phone_number, age)
        except:
            print('Something went wrong, try again')


def row_is_valid(row):
    return len(row) == 4 and \
           id_is_valid(row[0]) and \
           full_name_is_valid(row[1]) and \
           phone_number_is_valid(row[2]) and \
           age_is_valid(row[3])


def get_rows_from_csv_file(file):
    rows = []
    with open(file) as f:
        reader = csv.reader(f)
        try:
            rows = [row for row in reader if row_is_valid(row)]
        except:
            pass
    if not len(rows):
        print('File has no valid rows')
        return None
    else:
        return rows


add_employees_to_file = lambda rows: [add_employee_to_file(*row) for row in rows]


def delete_employee(id_to_delete):
    file_exist = check_file_exists(employee_json)
    if not file_exist:
        return

    employees_list = get_items_list_from_json_file(employee_json)
    employee_to_delete = get_employee_by_id(id_to_delete, employees_list)

    if employee_to_delete:
        answer = input('Are you sure you want to delete "{}"? y/n '.format(' '.join(employee_to_delete)))
        if answer == 'y':
            employees_list.remove(employee_to_delete)
            try:
                update_file_json(employees_list, employee_json)
                print('Employee {} was deleted'.format(id_to_delete))
            except:
                print('Something wrong with the file')
    else:
        print('Employee with ID {} not found'.format(id_to_delete))


def get_updated_json_content(employees_list, rows):
    count = 0
    employees_list_updated = employees_list
    for row in rows:
        employee_to_delete = employee_class.Employee(*row)
        employee_item = employee_to_delete.get_employee()
        if employee_item in employees_list:
            employees_list_updated.remove(employee_item)
            count += 1
    return count, employees_list_updated


def delete_employees_from_file(rows):
    file_exist = check_file_exists(employee_json)
    if not file_exist:
        return
    employees_list = get_items_list_from_json_file(employee_json)
    count, employees_list_updated = get_updated_json_content(employees_list, rows)
    if count:
        answer = input('Are you sure you want to delete {} employees? y/n '.format(count))
        if answer == 'y':
            try:
                update_file_json(employees_list_updated, employee_json)
                print('{} employees were deleted'.format(count))
            except:
                print('Something wrong with the file')
    else:
        print('None of employees in the given file was found')


def get_new_log_item(employee_id):
    today = datetime.today()
    enter_date = today.strftime("%d/%m/%Y")
    enter_time = today.strftime("%H:%M")
    new_time_log = employee_class.EmployeeTimeLog(employee_id, enter_date, enter_time)
    new_time_log_item = new_time_log.get_employee_time_log()
    return new_time_log_item


def get_current_month():
    today = datetime.today()
    current_month = today.strftime("%m/%Y")
    return current_month


def add_time_log(id_to_log):
    file_exist = check_file_exists(employee_json)
    if not file_exist:
        return
    employees_list = get_items_list_from_json_file(employee_json)
    employee_to_log = get_employee_by_id(id_to_log, employees_list)
    if not employee_to_log:
        print("ID {} doesn't appear in employees list".format(id_to_log))
        return
    new_time_log_item = get_new_log_item(id_to_log)
    logs_list = get_items_list_from_json_file(time_logs_json)
    logs_list.append(new_time_log_item)
    try:
        update_file_json(logs_list, time_logs_json)
        print('Time log added: ', *new_time_log_item.values())
    except:
        print('Something went wrong, try again')


def get_employee_details(id_to_log):
    employees_list = get_items_list_from_json_file(employee_json)
    employee_to_report = get_employee_by_id(id_to_log, employees_list)
    employee_details = id_to_log
    if employee_to_report:
        employee_details = employee_to_report['name'] + ' ' + employee_details
    return employee_details


def generate_report_for_employee(id_to_log):
    file_exist = check_file_exists(time_logs_json)
    if not file_exist:
        return
    logs_list = get_items_list_from_json_file(time_logs_json)
    employee_logs_list = list(filter(lambda r: r['id'] == id_to_log, logs_list))
    employee_details = get_employee_details(id_to_log)
    print('Attendance Report for', employee_details + ':')
    if len(employee_logs_list):
        for row in employee_logs_list:
            print(row['date'], row['time'])
    else:
        print('No logs to show')


def generate_report_for_current_month():
    file_exist = check_file_exists(time_logs_json)
    if not file_exist:
        return
    current_month = get_current_month()
    logs_list = get_items_list_from_json_file(time_logs_json)
    current_month_logs_list = list(filter(lambda r: r['date'].find(current_month) != -1, logs_list))
    print('Attendance Report for month', current_month + ':')
    if len(current_month_logs_list):
        for row in current_month_logs_list:
            employee_details = get_employee_details(row['id'])
            print(employee_details, row['date'].split('/')[0], row['time'])
    else:
        print('No logs to show')


def generate_report_for_late_employees():
    file_exist = check_file_exists(time_logs_json)
    if not file_exist:
        return
    logs_list = get_items_list_from_json_file(time_logs_json)
    late_logs_list = list(filter(lambda r: int(r['time'].split(':')[0]) > 9 or (
            int(r['time'].split(':')[0]) == 9 and int(r['time'].split(':')[1]) > 30), logs_list))
    print('Attendance Report for month employees who were late:')
    if len(late_logs_list):
        for row in late_logs_list:
            employee_details = get_employee_details(row['id'])
            print(employee_details, row['date'], row['time'])
    else:
        print('No logs to show')
