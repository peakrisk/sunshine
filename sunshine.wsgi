import sys
import os

path = '/var/www/sunshine'
sys.path.append(path)

os.chdir(path)

# Now cross fingers and import
from sunshine import app
from sunshine.settings import ProdConfig

application = app.create_app(ProdConfig)
