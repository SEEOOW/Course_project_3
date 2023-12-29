import json
from datetime import datetime


#Функция для выгрузки всех операций клиента
def load_all_operations(path):
    with open(path) as file:
        all_operations = json.load(file)
        return all_operations


#Функция для выявления операция клиента со статусом "Выполнено"
def executed_operations(operations_list):
    list_executed = []

    for operation in operations_list:
        if 'state' in operation and operation['state'] == 'EXECUTED':
        # if isinstance(operation, dict) and 'state' in operation and operation['state'] == 'EXECUTED':
            list_executed.append(operation)

    return list_executed


#Функция для сортировки операций клиента по дате
def sorted_operations(executed_operations):
    sorted_by_date = sorted(executed_operations, key=lambda operations: operations['date'], reverse=True)
    last_five_operations = sorted_by_date[:5]
    return last_five_operations


#Функция для приведения даты в нужный формат
def date_for_format(sorted_operations):
    formatted_date = datetime.strptime(sorted_operations, '%Y-%m-%dT%H:%M:%S.%f')
    formatted_date = formatted_date.strftime('%d.%m.%Y')
    return formatted_date


#Функция для "маскировки" номера карты и счета
def hidden_requisites(requisites: str):
    if not requisites.strip():
    # if requisites is None or not requisites.strip():
        return "None"
    else:
        requisites_split = requisites.split()
        only_number = requisites_split[-1]
        if requisites.lower().startswith("счет"):
            hided_number = f"**{only_number[-4:]}"
        else:
            hided_number = f"{only_number[:4]} {only_number[4:6]}** **** {only_number[-4:]}"

    return f'{" ".join(requisites_split[:-1])} {hided_number}'


#Функция для итогового вывода последних 5-ти операций клиента
def formatted_operations(sorted_operations):
    final_print = []

    for operation in sorted_operations:
        operation_date = date_for_format(operation['date'])
        operation_description = operation['description']
        line_one = f"{operation_date} {operation_description}"

        operation_from = hidden_requisites(operation.get('from', ' '))
        operation_to = hidden_requisites(operation['to'])
        line_two = f"{operation_from} -> {operation_to}"

        operation_amount = operation['operationAmount']['amount']
        operation_currency = operation['operationAmount']['currency']['name']
        line_three = f"{operation_amount} {operation_currency}"

        final_print.append(f"{line_one}\n{line_two}\n{line_three}\n")

    return '\n'.join(final_print)
