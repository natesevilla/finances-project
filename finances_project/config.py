import pygsheets
from logger import setup_logger

log = setup_logger(__file__)

def connect(file_name):
    try:
        # Create the Client
        log.info(f"Connecting to {file_name}")
        client = pygsheets.authorize(service_account_file="finances-442404-201151fbc89c.json") 
    except Exception as e:
        log.error(f"Unable to establish connection due to: {e}")  
    finally:
        # opens a spreadsheet by its name/title 
        spreadsht = client.open(file_name)
        title = client.spreadsheet_titles()
        log.info(f"Successfully connected to google sheet {title}!") 
    
        return spreadsht