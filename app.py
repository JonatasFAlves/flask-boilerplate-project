import os
from flask import Flask

from models.Articles import db
from routes import api_blueprint

# Init app
app = Flask(__name__)
app.config.from_object("config")

db.init_app(app)

app.register_blueprint(api_blueprint, url_prefix='/api')

# Run Server
if __name__ == '__main__':
  app.run(debug=True)