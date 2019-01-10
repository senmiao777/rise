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



def generate_entity_2_txt(file_path):

    print("file_path=", file_path)
    wb = load_workbook(file_path)
    sheet = wb.get_sheet_by_name('Sheet1')
    print("sheet=", sheet)

    json_field = '@JSONField(name = "{}")'
    perfix = 'private String {};\n'
    remark = '/** * {} */'

    for row in sheet.rows:
        property = row[0].value
        desc = row[3].value
        final_desc = remark.format(desc)
        final_json_field = json_field.format(property)
        hump_property = str2Hump(property)
        final_property = perfix.format(hump_property)

        final_str = final_desc + final_json_field + final_property

        print( final_str)


print("zhixing", generate_entity_2_txt('D:/test/apply.xlsx'))

