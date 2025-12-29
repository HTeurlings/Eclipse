import os
print("OS PATH:",os.environ["PATH"])
print("OS JAVA_HOME:",os.environ.get("JAVA_HOME"))

# print(os.environ["PATH"].replace(":","\n"))

import sys
print("Python version:",sys.version)

import shutil
print("Java version:",shutil.which("java"))

import subprocess
result = subprocess.run(["java","-version"], capture_output=True, text=True)
print(result.stderr)

