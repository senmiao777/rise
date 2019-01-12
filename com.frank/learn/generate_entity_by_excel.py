# coding=utf-8
import pymysql
from openpyxl import load_workbook
import json

def str2Hump(text):
    arr = text.split('_')
    res = ''
    for i in range(1, len(arr)):
        res = res + arr[i].capitalize()
        # res = res + arr[i]
    return arr[0] + res

def get_type(s):
    if s.find('BigDecimal') != -1:
        return 'BigDecimal'
    elif s.find('int') != -1:
        return 'Integer'
    elif s.upper().find('JSON') != -1:
        return 'Object'
    else:
        return 'String'



def generate_entity_2_txt(file_path):

    print("file_path=", file_path)
    wb = load_workbook(file_path)
    sheet = wb.get_sheet_by_name('Sheet1')
    print("sheet=", sheet)

    json_field = '@JSONField(name = "{}")'
    perfix = 'private {} {};\n'
    remark = '/** * {} */'

    for row in sheet.rows:
        property = row[0].value
        desc = row[3].value
        _type = row[1].value
        final_desc = remark.format(desc)
        final_json_field = json_field.format(property)
        hump_property = str2Hump(property)
        final_type = get_type(_type)
        final_property = perfix.format(final_type,hump_property)

        final_str = final_desc + final_json_field + final_property

        print( final_str)


print("zhixing", generate_entity_2_txt('D:/test/apply.xlsx'))

