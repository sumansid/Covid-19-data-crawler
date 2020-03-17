"""
Date : 15/04/2020
Author : Suman Sigdel
File : saveInExcel : Gets the data from covid19app.py file and saves the data in an excel file
"""

import covid19app

def save_in_excel():
    dict_with_data = covid19app.array_to_dict()
    with open('covid19_data.csv', 'w') as f:
        for key in dict_with_data.keys():
            f.write("%s,%s\n"%(key,dict_with_data[key]))

save_in_excel()





