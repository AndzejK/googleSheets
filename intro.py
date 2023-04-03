import pandas

# link to google spread sheet
main_url_to_google_sheet_file="https://docs.google.com/spreadsheets/d/1VFzR4GsVjfKY5ypsV_GflEg3dmsGfg24IG6zBFAZpBU/edit?usp=sharing"
sheet_name="2013_sheet1"
# gviz -> Google Visualization API query URL
# tq -> parameter in the URL indicates that the response should be in text format (CSV)
read_google_sheet_par=f"gviz/tq?tqx=out:csv&sheet={sheet_name}"
url_sheet_1=f"https://docs.google.com/spreadsheets/d/1VFzR4GsVjfKY5ypsV_GflEg3dmsGfg24IG6zBFAZpBU/{read_google_sheet_par}"
data=pandas.read_csv(url_sheet_1)
print(data)