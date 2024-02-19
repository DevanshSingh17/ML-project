import sys
#The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. 
# It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter. 

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    #exc_tb will provide on which file the roor has occured ,which line ..etc ,the before two details (_,_,) are not required 
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error occured in python script name[{0}] line number[{1}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    )
    
    return error_message
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        #print exception
        return self.error_message
    
    