# models/portfolio_model.py
from app import db
# from models.coin_model import Coin 
# from models.user_model import User
from datetime import datetime

class Portfolio(db.Model):
    __tablename__ = 'user_fav_coins'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    coin_id = db.Column(db.String(50), db.ForeignKey('coins_general.id'))
    quantity = db.Column(db.Float, nullable=False)
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow)

    # Define the relationship with the User model
    user = db.relationship('User', back_populates='portfolio')

    # Define the relationship with the Coin model
    coin = db.relationship('Coin', back_populates='portfolio')

    def __repr__(self):
        return f"<Portfolio(user_id={self.user_id}, coin_id={self.coin_id}, quantity={self.quantity})>"

    def calculate_total_value(self):
        pass
    