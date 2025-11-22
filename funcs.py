import pandas as pd
import dataframe_image as dfi


def create_table_money(tg_id, db_data):
    
    
    if db_data:
        data_table = {'Сумма': [],
                'Операция': [],
                'Время': []}
        
        for i in db_data:
            data_table['Сумма'].append(str(i[0]))
            data_table['Операция'].append(str(i[1]))
            data_table['Время'].append(str(i[2]))
    else:
        data_table = {'Сумма': ['-'],
                'Операция': ['-'],
                'Время': ['-']}

    df = pd.DataFrame(data_table)

    dfi.export(df, f'{tg_id}_table_mon_opr.png')