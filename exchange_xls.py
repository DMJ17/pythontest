import pymysql
import xlwt
import xlrd


def  Exchange_Xls():
    ExcelFile = xlrd.open_workbook(r'D:\python\project\test\test.xls',formatting_info=True)
    print(ExcelFile.sheet_names())
    sheet = ExcelFile.sheet_by_name('test')
    print(sheet.name,sheet.nrows,sheet.ncols)
    # for i in range(5):
    #     rows=sheet.row_values(i)
    #     print(rows)
    sheet2 = ExcelFile.sheet_by_index(0)
    rows_num = sheet2.nrows
    cols_num = sheet2.ncols

    for r in range(rows_num):
        entity_dict = {}
        for c in range(cols_num):
            cell_value = sheet2.row_values(r)[c]
            if(cell_value is None or cell_value == ''):
                cell_value = (get_merged_cells_value(sheet2, r, c))
            the_key = 'column' + str(c + 1)
            entity_dict[the_key] = cell_value

        print(entity_dict)


def get_merged_cells(sheet):
    return sheet.merged_cells

def get_merged_cells_value(sheet, row_index, col_index):
    merged  = get_merged_cells(sheet)
    for(rlow, rhigh, clow, chigh) in merged:
        if(row_index >= rlow and row_index < rhigh):
            if(col_index >= clow and row_index < chigh):
                cell_value = sheet.cell_value(rlow, clow)
                return cell_value
            break
    return None

Exchange_Xls()

