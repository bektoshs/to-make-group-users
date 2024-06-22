import pandas as pd

def read_and_process_file(file_name):

    df = pd.read_excel(file_name)

    df['Birthdate'] = pd.to_datetime(df['Birthdate'], format='%d.%m.%Y')
    df['Month_Day'] = df['Birthdate'].dt.strftime('%d.%m')

    df.rename(columns={'Name': 'Имя', 'Phone': 'Телефон', 'Status': 'Группа'}, inplace=True)

    for date in df['Month_Day'].unique():
        temp_df = df[df['Month_Day'] == date][['Имя', 'Телефон', 'Группа']]
        output_file_name = f'HB-{date}.2024.xlsx'
        temp_df.to_excel(output_file_name, index=False)
        print(f'Created: {output_file_name}')
    df.drop(columns=['Month_Day'], inplace=True)


file_name = 'Contacts.xls'
read_and_process_file(file_name)