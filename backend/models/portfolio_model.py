# models/portfolio_model.py
from app import db
from models.coin_model import Coin  # Import Coin model for the relationship
from models.user_model import User

class Portfolio(db.Model):
    __tablename__ = 'portfolio'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    coin_id = db.Column(db.String(50), db.ForeignKey('coins_general.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow)


    # Define the relationships
    user = db.relationship('User', back_populates='portfolio')
    coin = db.relationship('Coin', back_populates='portfolio')

    def __repr__(self):
        return f"<Portfolio(user_id={self.user_id}, coin_id={self.coin_id}, quantity={self.quantity})>"

    def calculate_total_value(self):
        # Implement logic to calculate the total value of the portfolio entry
        pass