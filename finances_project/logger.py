import logging
import os

def setup_logger(name: str, log_file: str = "app.log", level=logging.INFO):
    """Setup and return a logger instance."""
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    log_path = os.path.join("logs", log_file)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Prevent duplicate logs if multiple modules import the logger
    if not logger.hasHandlers():
        # File handler logs everything at 'level' (default INFO)
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(level)
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s"))
        
        # Console handler logs only errors and above
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)
        console_handler.setFormatter(logging.Formatter("%(filename)s - %(levelname)s - %(message)s"))
        
        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger
