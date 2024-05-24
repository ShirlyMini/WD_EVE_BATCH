from hybrid_framework.Utilities.XlUltility import *

#### get data from logindata.xlsx and convert to list of tuple

# xpath=r"C:\Users\user\PycharmProjects\pythonProject_WE_MARCH\hybrid_framework\TestData\LoginData.xlsx"
# sheet="Sheet1"

def load_data_from_xl(xpath, sheet):
    no_row = GetRow(xpath, sheet)
    no_col = GetCol(xpath, sheet)
    print(no_row, no_col)# 5 and 3
    data_list=[]
    for r in range(2, no_row+1):# 0 to 4....1-5
        temp_list=[]
        for c in range(1,no_col+1):
            #print(ReadData(xpath, sheet, r, c))
            temp_list.append(ReadData(xpath, sheet, r, c))
        # print(tuple(temp_list))
        data_list.append(tuple(temp_list))
    # print(data_list)
    return data_list

# load_data_from_xl(xpath,sheet)