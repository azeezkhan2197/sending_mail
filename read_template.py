import os
def get_template():
    path=os.path.join(os.getcwd(),"template\email.txt")
    return_text=open(path).read()
    return return_text