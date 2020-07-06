from notebooktoall.transform import transform_notebook
import os
import glob
import 2to3


def list_of_files():
    output = []
    for file in glob.glob("*.py"):
        output.append(file)
    return output

def convert2to3(lof):
    lof_size = (str(len(lof)))
    for count,item in enumerate(lof):
        if (count % 100) == 0:
            print(str(count) + "/ " + lof_size)
        try:
            transform_notebook(ipynb_file=item,
                               export_list=["py"])
        except:
            print(item)
        
        os.remove(item)