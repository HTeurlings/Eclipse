'''
Created on Jan 2, 2026

@author: henkt
'''

var1="Hello World !!"
print(var1)

import os
print("OS PATH:",os.environ["PATH"])
print("OS JAVA_HOME:",os.environ.get("JAVA_HOME"))

# print(os.environ["PATH"].replace(":","\n"))

import sys
print("Python version:",sys.version)

import shutil
print("Java version:",shutil.which("java"))

import subprocess
result1 = subprocess.run(["java","-version"], capture_output=True, text=True, check=True)
print(result1.stderr)
