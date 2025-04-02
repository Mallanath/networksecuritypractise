import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message: Exception, error_details: sys):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, error_details)

    def get_detailed_error_message(self, error_message: Exception, error_details: sys):
        _, _, exec_tb = error_details.exc_info()
        line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"
        return error_message

    def __str__(self):
        return self.error_message
        
# if __name__=='__main__':
#     try:
#         logger.logging.info("Enter the try block")
#         a=1/0
#         print("This will not be printed",a)
#     except Exception as e:
#            raise NetworkSecurityException(e,sys)