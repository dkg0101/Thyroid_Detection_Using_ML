import logging
from datetime import datetime 
import os 


LOG_FOLDER = 'thyroid_logs'
os.makedirs(LOG_FOLDER,exist_ok=True)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%s')}"


LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_FOLDER,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_FOLDER,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode='w',
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level= logging.INFO
                    )