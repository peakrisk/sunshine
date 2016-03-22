import sys
sys.path.append("/home/ec2-user/jng/sunshine")

# Activate the virtual environment
activate_this = '/home/ec2-user/.virtualenvs/sunshine/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

# Now cross fingers and import
from sunshine import app as application
