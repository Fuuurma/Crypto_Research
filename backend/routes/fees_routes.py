# routes/fees_routes.py

from flask import Blueprint, render_template
from models.fees_model import Fees
from models.fees_historic_model import Fees_Historic

fees_routes = Blueprint('fees', __name__)

@fees_routes.route('/fees', methods = ['GET', 'POST'])
def fees():
    fees = Fees.get_fees_data()
    fees_historic_plot = Fees_Historic.get_fees_historic_line_plot()
    fees_by_type = Fees.get_fees_by_type_plot()
    fees_by_category = Fees.get_fees_by_category_plot()
    return render_template('fees.html', fees=fees, fees_historic_plot = fees_historic_plot,
                           fees_by_type = fees_by_type, fees_by_category = fees_by_category )

