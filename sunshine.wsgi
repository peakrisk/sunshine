import sys
sys.path.append('/var/www/sunshine')

# Now cross fingers and import
from sunshine import app
from sunshine.settings import ProdConfig

application = app.create_app(ProdConfig)
