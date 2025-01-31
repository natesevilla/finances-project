# Importing required library 
import pygsheets
from constants import file_name, sheet_name

# Create the Client 
# Enter the name of the downloaded KEYS 
# file in service_account_file 
client = pygsheets.authorize(service_account_file="finances-442404-7c377f4e2e3f.json") 

# opens a spreadsheet by its name/title 
spreadsht = client.open(file_name)
title = client.spreadsheet_titles()
print(f"Opening google sheet {title}") 
  
# opens a worksheet by its name/title 
worksht = spreadsht.worksheet("title", sheet_name)

