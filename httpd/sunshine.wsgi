
# Activate the virtual environment
activate_this = '/home/ec2-user/.virtualenvs/sunshine/bin/activate_this.py'

with open(activate_this) as infile:
    exec(infile.read())

# Now cross fingers and import
from sunshine import app as application
