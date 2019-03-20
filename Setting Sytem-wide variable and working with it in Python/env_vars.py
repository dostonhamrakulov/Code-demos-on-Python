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
