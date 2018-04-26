#
# @Author: Fahad Ahammed 
# @Date: 2018-03-25 13:10:27 
# @Last Modified by:   Fahad Ahammed 
# @Last Modified time: 2018-03-25 13:10:27 
#

import sys
from flask import Flask

from blue.home.controllers import home
from blue.main.controllers import main


# Initiate App
# app = Flask(__name__)
app = Flask(__name__,
            instance_relative_config=True,
            template_folder='templates')

# Register Blueprint
app.register_blueprint(home)
app.register_blueprint(main)
