# modules/utils.py

import logging
import os

def setup_logging(log_file='logs/app.log'):
    # Ensure the logs directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a'
    )
    logging.info("Logging initialized.")
