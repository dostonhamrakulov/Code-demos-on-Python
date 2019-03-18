import subprocess

output = subprocess.getoutput('ls')
print(output)

num = output.count('d')
print("Number: ", num)


subprocess.check_output(["echo", "I am programmer"])


# More info:
# https://docs.python.org/2/library/subprocess.html#module-subprocess
