import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail:sys):
        # super().__init__(error_message)
        # self.error_message = self.get_detailed_error_message(error_message, error_detail)
        """
        Constructor for NetworkSecurityException class
        This is to be invoked whenever any of the other class methods ask for a
        NetworkSecurityException object to be created

        Parameters:
        error_message (str): The error message to be displayed
        error_detail (sys): The error detail to be displayed which is obtained
            from sys.exc_info()
        """
        self.error_message = error_message
        _,_,exc_tb = error_detail.exc_info()
        
        self.line_number = exc_tb.tb_frame.f_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
        
if __name__ == "__main__":
    try:
        logger.logging.info("Trying to divide by zero")
        a = 1/0
    except Exception as e:
        raise NetworkSecurityException(e, sys)