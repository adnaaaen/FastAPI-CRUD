import logging
import os

logging_format = "%(asctime)s : %(levelname)s : %(message)s : %(module)s : %(lineno)d"
log_folder = "logs"
log_filepath = os.path.join(log_folder, "app.log")
os.makedirs(log_folder, exist_ok=True)
logging.basicConfig(format=logging_format, handlers=[logging.FileHandler(log_filepath)])
logger = logging.getLogger(__name__)
