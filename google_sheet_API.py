#console.cloud.google.com
"""
    ### Create a Service Account ###
1. I have created a new project, "Python".
2. I have enabled APIS AND SERVICES.
3. Then I searched and found "Google Drive API". 
4. I enabled "Google Drive API" for the project "Python".
5. Once it was enabled I created credentials for this API by selecting API -> "Google Drive API"
6. After naming Service Acc I chose a role for this project "Python" as project/Editor
7. Under Service Account I chose a new created acc / KEYS
8. I create a new JSON Key and automatically downloaded to my MAC
9. I have enabled Google Sheet API this time
10. I have gone to my google sheets acc and invited Service Account via email in order to give access to this google sheet, which
I found in JSON file as "client_email"
11. I gave permissions "Editor" to this email/service
"""
import gspread
# Establishing connection to Google Sheet, adding JSON <location/name> - API_key_project_Python.json
gc=gspread.service_account("API_key_project_Python.json")
# all sheets/entire sheet
spreadsheet=gc.open("weather_public_edu") 

# get a sheet by ID
worksheet1_id=spreadsheet.get_worksheet(0) # we get here an object <Worksheet '2013_sheet1' id:1055298144>

# get a sheet by the name
worksheet2_name=spreadsheet.worksheet("2014_sheet2")

# fetch data from the worksheet1_id object
data_sheet_1=worksheet1_id.get_all_records()

# fetch data from the worksheet2_name object
data_sheet_2=worksheet2_name.get_all_records()

# Get the specific values/cells - One row
data_sheet_2=worksheet2_name.get_values("A7:F7") #data type List in the List

# Get more than one row (>1), let's say 4 rows = Select 1st Cell and the Last Cell :)
data_sheet_2=worksheet2_name.get_values("A7:F10") # Data type - List which has multiple list and our case 4 list in one List

# Get ROW by INDEX
a_row_by_index=worksheet2_name.row_values(2)

# Get a column by  CELLS
a_column=worksheet2_name.get_values("A1:A23") # not the best method of getting columns

# Get a column by INDEX
a_column=worksheet2_name.col_values(1)[1:] # based on an index, starts from 1 but if I don't want the header then I can applu slice method and start from where I want to
print(a_row_by_index)