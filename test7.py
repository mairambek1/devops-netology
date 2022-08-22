#!/usr/bin/env python3

import os

bash_command = ["cd ~/devops-netology", "pwd", "git status"]            
result_os = os.popen(' && '.join(bash_command)).read()
#is_change = False                                             
cwd=result_os.split('\n')                                      
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = cwd[0]+'/'+result.replace('\tmodified:   ', '')
        print(prepare_result)
        #break          
