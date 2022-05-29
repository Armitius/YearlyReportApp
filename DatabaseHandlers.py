import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

def get_sheet_from_database(spreadsheet_name,worksheet_name):
    # Create scope
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # create some credential using that scope and content of startup_funding.json
    creds = ServiceAccountCredentials.from_json_keyfile_name('DataBaseConnection.json', scope)
    # create gspread authorize using that credential
    client = gspread.authorize(creds)
    # Now will can access our google sheets we call client.open on StartupName
    sheet = client.open(spreadsheet_name).worksheet(worksheet_name)
    return sheet

# def next_available_row(sheet, col_min, col_max):
#   # looks for empty row based on values appearing in 1st N columns
#   cols = sheet.range(1, 1, sheet.row_count, cols_to_sample)
#   return max([cell.row for cell in cols if cell.value]) + 1

def insert_new_transaction(worksheet ,transaction_type, date, amount, description = '', category = '', subcategory = ''):
    col_min=''
    if(transaction_type == 'Uitgave'):
        col_min = 'B'

    if (transaction_type == 'Inkomst'):
        col_min = 'H'


    if (transaction_type == 'Niet-Uitgave'):
        col_min = 'N'

    insertRow = [date, amount, description, category, subcategory]
    worksheet.append_row(insertRow, table_range= col_min + '4', value_input_option='USER_ENTERED')

def get_categories(worksheet, col_value):
    categories_list = worksheet.col_values(col_value)
    categories_list = list(dict.fromkeys(categories_list))
    return categories_list

def get_subcategories(worksheet, chosen_category):
    subcategories_list = worksheet.get_all_values()
    subcategories_list = list(filter(lambda c: c[0] == chosen_category, subcategories_list))
    final_subcategories_list = []
    for item in range(len(subcategories_list)):
        add = str(subcategories_list[item][1])
        final_subcategories_list.append(add)
    return final_subcategories_list


#Now will can access our google sheets we call client.open on StartupName ).worksheet()
# sheet = get_sheet_from_database('Jaarlijkse begroting 2022', 'Transacties')
# sheet2 = get_sheet_from_database('Jaarlijkse begroting 2022', 'Opties')
# result = sheet.col_values(2)
# pp = pprint.PrettyPrinter()
#Access all of the record inside that
# date=datetime.date(2022,5,22),
# insert_new_transaction('Inkomst', '22-05-2022', 485, 'Terugbetaling oma', 'Terugbetaling', 'Terugbetaling')
# categories = get_categories(sheet2,1)
# category = 'Gezondheid'
# subcategories = get_subcategories(sheet2, category)


# pp = pprint.PrettyPrinter()
# pp.pprint(result)

# row = next_available_row(sheet)
# pp.pprint(categories)
# pp.pprint(subcategories)
# pp.pprint(row)



