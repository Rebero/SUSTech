#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from IPython.core.display import display, HTML

run_code_str = '''
<form action="javascript:Jupyter.notebook.execute_cell()"><input type ="submit" id="runButton" value="Run Cell"></form>
'''

display(HTML(run_code_str))

def run_code():
    display(HTML(run_code_str))

