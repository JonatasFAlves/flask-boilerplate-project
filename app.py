import os
from flask import Flask

from models.Article import db
from routes import api_blueprint

# Init app
app = Flask(__name__)
app.config.from_object("config")

db.init_app(app)

with app.app_context():
  db.create_all()

app.register_blueprint(api_blueprint, url_prefix='/api')

# Run Server
if __name__ == '__main__':
  print("Please access http://localhost:5000/api/status")
  app.run(debug=True)