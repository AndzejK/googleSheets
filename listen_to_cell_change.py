import gspread
import time
# Establishing connection to Google Sheet, adding JSON <location/name> - API_key_project_Python.json
gc=gspread.service_account("API_key_project_Python.json")
# all sheets/entire sheet
spreadsheet=gc.open("weather_public_edu") 
# get a sheet by ID
worksheet1_id=spreadsheet.get_worksheet(0) # name of it is "2013_sheet1"

# If G26 cell will change its value the sheet "watch" will be update to for a particular cell
# get a sheet by the name
worksheet2_name=spreadsheet.worksheet("watch")
# in order to get the change it means python has to run infenetly this script
while True:
    value1=worksheet1_id.acell("G26").value #get the value of this cell, G26
    time.sleep(2)
    value2=worksheet1_id.acell("G26").value 
    if value1!=value2:
        worksheet2_name.update("A1",'Changed!')
        print("changed: "+value2)
