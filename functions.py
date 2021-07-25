import csv
import os.path
import add_functions


def add_employee():
    employee_id, full_name, phone_number, age = add_functions.enter_employee_details()
    add_functions.add_employee_to_file(employee_id, full_name, phone_number, age)


def add_employee_file():
    file_path = add_functions.enter_file_path()
    rows = add_functions.get_rows_from_csv_file(file_path)
    if rows:
        add_functions.add_employees_to_file(rows)


def delete_employee():
    id_to_delete = add_functions.enter_id()
    add_functions.delete_employee(id_to_delete)


def delete_employee_file():
    file_path = add_functions.enter_file_path()
    rows = add_functions.get_rows_from_csv_file(file_path)
    if rows:
        add_functions.delete_employees_from_file(rows)


def mark_attendance():
    id_to_log = add_functions.enter_id()
    add_functions.add_time_log(id_to_log)


def generate_report():
    id_to_log = add_functions.enter_id()
    add_functions.generate_report_for_employee(id_to_log)


def print_report_month():
    add_functions.generate_report_for_current_month()


def print_report_late():
    add_functions.generate_report_for_late_employees()
