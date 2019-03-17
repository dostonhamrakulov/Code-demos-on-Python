# how to set Environment Variables in Ubuntu or in linux

### Description:
We will set **enviroment variables** in ubuntu.\
\
A suitable file for environment variable settings that affect the system as a whole (rather than just a particular user) is **/etc/environment**. An alternative is to create a file for the purpose in the /etc/profile.d directory.


* set variable only for current shell:
```[Python]
$ VARNAME="my value"
```
* To set it for current shell and all processes started from current shell:
```[Python]
$ export VARNAME="my value"      # shorter, less portable version
```

* To set it permanently for all future bash sessions add such line to your .bashrc file in your $HOME directory.

* To set it permanently, and system wide (all users, all processes) add set variable in /etc/environment:
```[Python]
$ sudo -H gedit /etc/environment
```
**In case error**
You should disable access control, so that clients can connect from any host
```[Python]
$ xhost +
```
* This file only accepts variable assignments like:
```[Python]
VARNAME="my value"
```
* Do not use the **export** keyword here.
* You need to **logout** from current user and login again so environment variables changes take place.\


### Accessing enviroment variables via Python script:
**/etc/environment** looks like this:
```[Python]
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"
DB_USER="DB_USER_NAME"
DB_PASS="PASSWORD_HERE"
MY_VALUE="Doston Hamrakulov"
```
**Python** script:
```python
import os

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')
secret_key = os.environ.get('SECRET_KEY')
debug_value = os.environ.get('DEBUG_VALUE')
my_value = os.environ.get('MY_VALUE')

print(db_user)
print(db_password)
print(secret_key)
print(debug_value)
print(my_value)
```

### Programming languages and frameworks
```[Python]
Python
```

### IDE
```[Vim]
Vim
```

## Author
**Doston Hamrakulov**
>*Software Engineer, Web Developer, Freelancer*

