import gspread
import statistics
# Establishing connection to Google Sheet, adding JSON <location/name> - API_key_project_Python.json
gc=gspread.service_account("API_key_project_Python.json")
# all sheets/entire sheet
spreadsheet=gc.open("weather_public_edu") 
# get a sheet by ID
worksheet1_id=spreadsheet.get_worksheet(0) # name of it is "2013_sheet1"

# Task No.1 - Calculate mean Temprature,F and add this value at the end 

# get G column, Temperature,F - based on ID and ignore the header
temp_f_G=worksheet1_id.col_values(7)[1:] # The list that has the values a str
temp_f_G_float=[float(i)for i in temp_f_G]
mean_value=statistics.mean(temp_f_G_float)

# add mean value to the end
new_cell_mean_value=worksheet1_id.update("G26",mean_value)


