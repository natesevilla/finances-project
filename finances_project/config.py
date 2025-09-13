import pygsheets
from logger import setup_logger

logger = setup_logger(__file__)

def connect(file_name):
    try:
        # Create the Client 
        client = pygsheets.authorize(service_account_file="finances-442404-201151fbc89c.json") 
    except Exception as e:
        logger.error(f"Unable to establish connection due to: {e}")  
    finally:
        # opens a spreadsheet by its name/title 
        spreadsht = client.open(file_name)
        title = client.spreadsheet_titles()
        logger.info(f"Connected to google sheet {title}") 
    
        return spreadsht