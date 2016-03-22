import sys
sys.path.append('/var/www/sunshine')

# Activate the virtual environment
activate_this = '/var/www/sunshine/venv/bin/activate_this.py'

with open(activate_this) as infile:
    exec(infile.read())

# Now cross fingers and import
from sunshine import app as application
