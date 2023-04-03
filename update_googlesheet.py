import gspread
# Establishing connection to Google Sheet, adding JSON <location/name> - API_key_project_Python.json
gc=gspread.service_account("API_key_project_Python.json")
# all sheets/entire sheet
spreadsheet=gc.open("weather_public_edu") 
# get a sheet by ID
worksheet1_id=spreadsheet.get_worksheet(0) # name of it is "2013_sheet1"

# Update a cell by its name/cordinate, E5
#mod_cell=worksheet1_id.update('E5',-30)

# Update a cell based on Row_column
#mod_cel=worksheet1_id.update_cell(5,5,"31")

# Add and update the column, like convertig values from C to F
existing_col=worksheet1_id.get_values("E2:E25") # Data in the List where we have the multiple list with values as a str
# since we want to create another list from the given list we can Pythonic syntex like - LIST COMPREHANSION in one line
new_col=[[round((float(i[0])*9/5+32),1)] for i in existing_col] # loop through a list and what to do with "i" - aply formula to convert from C to F
# instead of updating E2:E25 values I'll add a new collum G2:G25
new_col_G=worksheet1_id.update("G1:G25",[["Temperature,F"]]+new_col) # adding the header and values

update_E_header_name=worksheet1_id.update('E1',"Temperature,C")
