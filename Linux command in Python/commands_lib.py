# Deprecated since version 2.6: The "commands" module has been removed in Python 3. Use the "subprocess" module instead.

import commands

output = commands.getoutput('ls')
print(output)

num = output.count('d')
print("Number: ", num)

soe = commands.getstatusoutput('ifconfig')
print("=========================================")
print(soe)

