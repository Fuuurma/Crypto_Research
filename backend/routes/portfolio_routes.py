# routes/portfolio_routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models.coin_model import Coin
from models.user_model import User
from app import db

portfolio_routes = Blueprint('portfolio', __name__)

@portfolio_routes.route('/portfolio/<int:user_id>')
def user_portfolio(user_id):
    user = User.query.get_or_404(user_id)
    portfolio = user.portfolio
    
    favorite_coins = user.favorite_coins  # Assuming you have a relationship defined

    # Include logic to calculate portfolio statistics (total value, ROI, etc.)
    total_portfolio_value = calculate_total_portfolio_value(user)
    portfolio_roi = calculate_portfolio_roi(user)
    
    return render_template('portfolio.html', user=user, portfolio=portfolio)



@portfolio_routes.route('/search', methods=['POST'])
def search():
    search_query = request.form.get('search_query')

    # Perform a search in the Coin table based on the search_query
    search_results = Coin.query.filter(Coin.name.ilike(f'%{search_query}%')).all()

    return render_template('search_results.html', search_results=search_results)



@portfolio_routes.route('/add_to_favorites/<int:user_id>/<int:coin_id>')
def add_to_favorites(user_id, coin_id):
    user = User.query.get_or_404(user_id)
    coin = Coin.query.get_or_404(coin_id)

    # Check if the coin is already in the user's favorites
    if coin not in user.favorite_coins:
        user.favorite_coins.append(coin)
        db.session.commit()

    return redirect(url_for('portfolio.user_portfolio', user_id=user_id))

#    {{ coin.name }} - <a href="{{ url_for('portfolio.add_to_favorites', user_id=user.id, coin_id=coin.id) }}">Add to Favorites</a>


@portfolio_routes.route('/portfolio')
@login_required
def portfolio_dashboard():
    # Retrieve user's favorite coins and other relevant data
    user = User.query.get(current_user.id)
    favorite_coins = user.favorite_coins  # Assuming you have a relationship defined

    return render_template('portfolio_dashboard.html', favorite_coins=favorite_coins)