import logging
import os


class LogGen:

    @staticmethod
    def loggen():
        basedir = os.path.dirname(os.path.dirname(__file__))
        log_dir = os.path.join(basedir,"Logs")
        os.makedirs(log_dir,exist_ok=True)

        log_file = os.path.join(log_dir,"Automation.log")

        logger  = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            fhandler =  logging.FileHandler(filename=log_file,mode='a')
            formatter = logging.Formatter("%(asctime)s -%(filename)s -%(levelname)s - %(message)s")
            fhandler.setFormatter(formatter)
            logger.addHandler(fhandler)
        return  logger

