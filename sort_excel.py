import pandas as pd
from datetime import datetime

# 1. Define the participant data from both images
data = [
    # --- Data from Image 1 ---
    {"Name": "Aariv Mukherjee", "Gender": "Boy", "Date of Birth": "03/10/2021", "CHSS No.": "19585D", "Flat No.": "D 16", "Mobile No.": "8369394862"},
    {"Name": "Dyuthi renjith", "Gender": "Girl", "Date of Birth": "04/28/2019", "CHSS No.": "15928C", "Flat No.": "D07", "Mobile No.": "9699496480"},
    {"Name": "Mishika Srivastava", "Gender": "Girl", "Date of Birth": "12/21/2019", "CHSS No.": "19572C", "Flat No.": "A-13", "Mobile No.": "737636915"},
    {"Name": "SRESHA S SINGH", "Gender": "Girl", "Date of Birth": "07/01/2020", "CHSS No.": "14610D", "Flat No.": "A-14", "Mobile No.": "989283610"},
    {"Name": "Shivansh Kumar", "Gender": "Boy", "Date of Birth": "01/09/2020", "CHSS No.": "21243D", "Flat No.": "D/1 mansarover", "Mobile No.": "975705501"},
    {"Name": "AADHYA KIRAN SANE", "Gender": "Girl", "Date of Birth": "03/28/2018", "CHSS No.": "19832C", "Flat No.": "D-03", "Mobile No.": "9890884517"},
    {"Name": "Yutika Sarpole", "Gender": "Girl", "Date of Birth": "07/24/2018", "CHSS No.": "30526D", "Flat No.": "D/26", "Mobile No.": "998740950"},
    {"Name": "Augadh Sahoo", "Gender": "Boy", "Date of Birth": "05/03/2017", "CHSS No.": "4223D", "Flat No.": "B-23", "Mobile No.": "996984964"},
    {"Name": "Panshul Sarpole", "Gender": "Boy", "Date of Birth": "06/13/2016", "CHSS No.": "30526C", "Flat No.": "D/26", "Mobile No.": "998740950"},
    {"Name": "Omkar D Prasad", "Gender": "Boy", "Date of Birth": "11/26/2015", "CHSS No.": "19246D", "Flat No.": "B 7", "Mobile No.": "9757425008"},
    {"Name": "SWARAA S SINGH", "Gender": "Girl", "Date of Birth": "09/29/2015", "CHSS No.": "14610C", "Flat No.": "A-14", "Mobile No.": "989283610"},
    {"Name": "AradhyaShaileshRamugade", "Gender": "Boy", "Date of Birth": "02/10/2015", "CHSS No.": "14975D", "Flat No.": "C 23", "Mobile No.": "8169124009"},
    {"Name": "Kanishk Molke", "Gender": "Boy", "Date of Birth": "11/20/2014", "CHSS No.": "12717D", "Flat No.": "C/06", "Mobile No.": "989277216"},
    {"Name": "Anay Harer", "Gender": "Boy", "Date of Birth": "08/21/2014", "CHSS No.": "3866D", "Flat No.": "A 8", "Mobile No.": "773855576"},
    {"Name": "Anvi Harer", "Gender": "Girl", "Date of Birth": "08/21/2014", "CHSS No.": "3866C", "Flat No.": "A 8", "Mobile No.": "773855576"},
    {"Name": "Ayush Kumar jyoti", "Gender": "Boy", "Date of Birth": "08/07/2013", "CHSS No.": "18967B", "Flat No.": "D - 32", "Mobile No.": "913681564"},
    {"Name": "Tejasvi D Prasad", "Gender": "Girl", "Date of Birth": "07/18/2013", "CHSS No.": "19246C", "Flat No.": "B 7", "Mobile No.": "9757425008"},

    # --- Data from Image 2 ---
    {"Name": "Adhrit Sahoo", "Gender": "Boy", "Date of Birth": "10/20/2020", "CHSS No.": "10/7719D", "Flat No.": "D-2", "Mobile No.": "8850146518"},
    {"Name": "Vivya Vasava", "Gender": "Girl", "Date of Birth": "08/14/2020", "CHSS No.": "9/14993D", "Flat No.": "A-21", "Mobile No.": "8369312122"},
    {"Name": "Aayush Sunil Vitmal", "Gender": "Boy", "Date of Birth": "03/02/2020", "CHSS No.": "12/3403D", "Flat No.": "A11", "Mobile No.": "8356995332"},
    {"Name": "Siddhant Jadhav", "Gender": "Boy", "Date of Birth": "10/31/2019", "CHSS No.": "9/16853D", "Flat No.": "D-25", "Mobile No.": "9618736183"},
    {"Name": "ANUSHREE ANAND SATPUTE", "Gender": "Girl", "Date of Birth": "10/06/2019", "CHSS No.": "9/16257D", "Flat No.": "A/10", "Mobile No.": "9702315854"},
    {"Name": "Aradhy Sunil Vitmal", "Gender": "Boy", "Date of Birth": "10/18/2017", "CHSS No.": "12/3403C", "Flat No.": "A11", "Mobile No.": "8356995332"},
    {"Name": "Mohd Arsalaan Quazi", "Gender": "Boy", "Date of Birth": "08/17/2017", "CHSS No.": "12/4577D", "Flat No.": "A-1", "Mobile No.": "9969728618"},
    {"Name": "AVIN MAZUMDAR", "Gender": "Boy", "Date of Birth": "07/18/2016", "CHSS No.": "10/7602D", "Flat No.": "C-16 Manasarovar", "Mobile No.": "8369436375"},
    {"Name": "Vedika Narendra Hedau", "Gender": "Girl", "Date of Birth": "03/15/2016", "CHSS No.": "2/3867-D", "Flat No.": "D31", "Mobile No.": "8451871380"},
    {"Name": "Mansi Bhushan Shinde", "Gender": "Girl", "Date of Birth": "09/13/2015", "CHSS No.": "14/1414D", "Flat No.": "D 15", "Mobile No.": "8097001984"},
    {"Name": "Manas Bhushan Shinde", "Gender": "Boy", "Date of Birth": "09/13/2015", "CHSS No.": "14/1414C", "Flat No.": "D 15", "Mobile No.": "8097001984"},
    {"Name": "Sanavi Rakesh Mahagaonkar", "Gender": "Girl", "Date of Birth": "10/05/2014", "CHSS No.": "11/3630E", "Flat No.": "B-5", "Mobile No.": "9969032341"},
    {"Name": "Tanmay Sanjay Sawant", "Gender": "Boy", "Date of Birth": "08/05/2014", "CHSS No.": "7/13466D", "Flat No.": "C24", "Mobile No.": "8108145778"},
    {"Name": "Suhanya Sahoo", "Gender": "Girl", "Date of Birth": "04/13/2014", "CHSS No.": "10/7719C", "Flat No.": "D-2", "Mobile No.": "8850146518"},
    {"Name": "ARNAV ANAND SATPUTE", "Gender": "Boy", "Date of Birth": "03/02/2014", "CHSS No.": "9/16257C", "Flat No.": "A/10", "Mobile No.": "9702315854"},
    {"Name": "Vaishnavi Deore", "Gender": "Girl", "Date of Birth": "03/17/2013", "CHSS No.": "14/952D", "Flat No.": "C-20", "Mobile No.": "9869967601"},
    {"Name": "Kirti Bharat Rajole", "Gender": "Girl", "Date of Birth": "11/14/1988", "CHSS No.": "14/1474B", "Flat No.": "B 17", "Mobile No.": "91378 68093"},
    {"Name": "Alka Rajole", "Gender": "Girl", "Date of Birth": "06/16/1962", "CHSS No.": "14/1474M", "Flat No.": "B 17", "Mobile No.": "91378 68093"}
]

# 2. Create DataFrame
df = pd.DataFrame(data)

# 3. Convert 'Date of Birth' to datetime objects
df['Date of Birth'] = pd.to_datetime(df['Date of Birth'])

# 4. Define current date for age calculation
current_date = pd.Timestamp("2025-11-23")

# 5. Function to calculate age in Years and Months
def calculate_age_str(born, current):
    years = current.year - born.year
    months = current.month - born.month
    if current.day < born.day:
        months -= 1
    if months < 0:
        years -= 1
        months += 12
    return f"{years} Years, {months} Months"

# Apply age calculation
df['Age'] = df['Date of Birth'].apply(lambda x: calculate_age_str(x, current_date))

# 6. Sort by Age (Youngest first means most recent birth date first)
df = df.sort_values(by='Date of Birth', ascending=False)

# 7. Format Date of Birth back to string for clean display
df['Date of Birth'] = df['Date of Birth'].dt.strftime('%m/%d/%Y')

# 8. Reorder columns (excluding Timestamp)
df = df[['Name', 'Gender', 'Age', 'Date of Birth', 'CHSS No.', 'Flat No.', 'Mobile No.']]

# 9. Display the sorted data


# Optional: Export to Excel
df.to_excel("Sorted_Combined_List.xlsx", index=False)