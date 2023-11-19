# routes/test_routes.py

from flask import Blueprint, render_template
from models.pools_model import Pool

pools_routes = Blueprint('pools', __name__)

@pools_routes.route('/pools')
def pools():
    pools = Pool.query.limit(5).all()
    return render_template('pools.html', pools=pools)
