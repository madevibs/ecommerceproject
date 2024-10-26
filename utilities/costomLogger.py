import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger("automation")
        logger.setLevel(logging.INFO)  # Set the log level

        # Create a file handler or console handler
        handler = logging.FileHandler(
            "C:\\Users\\KITS\\PycharmProjects\\ecommerceproject\\Logs\\automation.log")  # Logs will be written to this file
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # Add the handler to the logger
        if not logger.handlers:  # To prevent adding multiple handlers
            logger.addHandler(handler)

        return logger
