import pandas as pd
from datetime import datetime

# 1. Data Entry (Transcribed from the document)
data_drawing = [
    {"Name": "Aariv Mukherjee", "Birth Date": "10-03-2021", "Flat No": "B 7 Manasarovar", "Mobile No": "9757425008"},
    {"Name": "Avin Mazumdar", "Birth Date": "14-08-2020", "Flat No": "C-16 Manasarovar", "Mobile No": "8369436374"},
    {"Name": "Vivya Vasava", "Birth Date": "14-08-2020", "Flat No": "A-21", "Mobile No": "8369312122"},
    {"Name": "Akshat Bhoir", "Birth Date": "19-03-2020", "Flat No": "B-6", "Mobile No": "9618736183"},
    {"Name": "Aayush Sunil Vitmal", "Birth Date": "02-03-2020", "Flat No": "A 11", "Mobile No": "8356995332"},
    {"Name": "Shivansh Kumar", "Birth Date": "09-01-2020", "Flat No": "B 7 Manasarovar", "Mobile No": "9757055015"},
    {"Name": "Mishika Srivastava", "Birth Date": "21-12-2019", "Flat No": "A 13", "Mobile No": "7376369156"},
    {"Name": "Sana Shekh", "Birth Date": "14-12-2019", "Flat No": "B 16", "Mobile No": "9833584614"},
    {"Name": "Sidhant Jadhav", "Birth Date": "31-10-2019", "Flat No": "D-25", "Mobile No": "9618736183"},
    {"Name": "Dyuthi renjith", "Birth Date": "28-04-2019", "Flat No": "D 16", "Mobile No": "9699496480"},
    {"Name": "Augadh Sahoo", "Birth Date": "24-07-2018", "Flat No": "D/26", "Mobile No": "9987409506"},
    {"Name": "AADHYA KIRAN SANE", "Birth Date": "28-03-2018", "Flat No": "B 7 Manasarovar", "Mobile No": "9890884517"},
    {"Name": "Sresha S Singh", "Birth Date": "18-10-2017", "Flat No": "A-14", "Mobile No": "9136815645"},
    {"Name": "Aradhy Sunil Vitmal", "Birth Date": "18-10-2017", "Flat No": "A 11", "Mobile No": "8356995332"},
    {"Name": "Yutika Sarpole", "Birth Date": "03-05-2017", "Flat No": "D/26", "Mobile No": "9987409506"},
    {"Name": "Panshul Sarpole", "Birth Date": "13-06-2016", "Flat No": "D/26", "Mobile No": "9987409506"},
    {"Name": "Omkar D Prasad", "Birth Date": "26-11-2015", "Flat No": "B 7 Manasarovar", "Mobile No": "9757425008"},
    {"Name": "Swaraa S Singh", "Birth Date": "29-09-2015", "Flat No": "A-14", "Mobile No": "9136815645"},
    {"Name": "Manas Bhushan Shinde", "Birth Date": "13-09-2015", "Flat No": "C 24", "Mobile No": "8097001984"},
    {"Name": "Mansi Bhushan Shinde", "Birth Date": "13-09-2015", "Flat No": "C 24", "Mobile No": "8097001984"},
    {"Name": "Aradhya ShaileshRamugade", "Birth Date": "10-02-2015", "Flat No": "C 23", "Mobile No": "8169124009"},
    {"Name": "Anvi Harer", "Birth Date": "21-08-2014", "Flat No": "A 8", "Mobile No": "7738555761"},
    {"Name": "Anay Harer", "Birth Date": "21-08-2014", "Flat No": "A 8", "Mobile No": "7738555761"},
    {"Name": "Tanmay Sanjay Sawant", "Birth Date": "05-08-2014", "Flat No": "C 24", "Mobile No": "8108145778"},
    {"Name": "Ayush Kumar jyoti", "Birth Date": "07-08-2013", "Flat No": "D - 32", "Mobile No": "9892836107"},
    {"Name": "Tejasvi D Prasad", "Birth Date": "18-07-2013", "Flat No": "B 7 Manasarovar", "Mobile No": "8369394862"},
    {"Name": "Inaya Shekh", "Birth Date": "09-05-2013", "Flat No": "B 16", "Mobile No": "9768107813"},
    {"Name": "Vaishnavi Deore", "Birth Date": "17-03-2013", "Flat No": "C-20", "Mobile No": "9869967601"}
]

# 2. Create DataFrame
df = pd.DataFrame(data_drawing)

# 3. Setup Dates
df['Birth Date'] = pd.to_datetime(df['Birth Date'], format='%d-%m-%Y')
current_date = pd.Timestamp("2025-11-23")

# 4. Calculate Age Function
def calculate_age_str(born, current):
    years = current.year - born.year
    months = current.month - born.month
    if current.day < born.day:
        months -= 1
    if months < 0:
        years -= 1
        months += 12
    return f"{years} Years, {months} Months"

# 5. Apply Logic & Sort
df['Calculated Age'] = df['Birth Date'].apply(lambda x: calculate_age_str(x, current_date))
df = df.sort_values(by='Birth Date', ascending=False) # Youngest First

# 6. Clean up for Export
df['Birth Date'] = df['Birth Date'].dt.strftime('%d-%m-%Y')
df = df[['Name', 'Birth Date', 'Calculated Age', 'Flat No', 'Mobile No']]

# 7. Export
df.to_excel('Sorted_Drawing_Participants_Detailed.xlsx', index=False)