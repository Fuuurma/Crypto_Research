# from app import db
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin
# # from models.portfolio_model import Portfolio
# from models.coin_model import Coin
# from app import db

# class User(db.Model, UserMixin):
#     __tablename__ = 'user'
    
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128), nullable=False)
    
#     # Define the many-to-many relationship with coins through 'user_fav_coins' table
#     favorite_coins = db.relationship('Coin', secondary='user_fav_coins', back_populates='users')

#     # Define the one-to-many relationship with portfolio
#     portfolio = db.relationship('Portfolio', back_populates='user')
    
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
    
#     def is_favorite_coin(self, coin_id):
#         return Coin.query.filter_by(id=coin_id).first() in self.favorite_coins
