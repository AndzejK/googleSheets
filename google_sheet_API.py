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
print(data_sheet_2[10])