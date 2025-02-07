import sys

def error_message(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = "Error occurred in python script at [{0}] line number [{1}] with error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_msg



class CustomException(Exception):
    def __init__(self,error_msg, error_detail: sys):
        super.__init__(error_msg)
        self.error_msg = error_message(error_msg, error_detail)
        
    def __str__(self):
        return super().__str__() + " " + self.error_msg 