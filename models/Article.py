from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from marshmallow import fields, validate

db = SQLAlchemy()
ma = Marshmallow()

# Article Class/Model
class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    price = db.Column(db.Float)

    def __repr__(self):
        return "Article: {} {}c".format(self.name, self.price)

# Article Schema
class ArticleSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(1))
    price = fields.Float(required=True)