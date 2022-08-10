#!/usr/bin/env python3

import os
import sys

path = "./"
if len(sys.argv) >= 2:
    path = sys.argv[1]
    if not os.path.isdir(path):
          sys.exit("Directory doesn't exist: " + path)

bash_command = ["cd " + path, "git status 2>&1"]
git_command = ["git rev-parse --show-toplevel"]

result_os = os.popen(' && '.join(bash_command)).read()
if result_os.find('not a git') != -1:
    sys.exit("not a git repository: " + path)

git_top_level = (os.popen(' && '.join(git_command)).read()).replace('\n', '/')

for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(git_top_level + prepare_result)

