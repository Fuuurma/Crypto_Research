# routes/fees_routes.py

from flask import Blueprint, render_template
from models.fees_model import Fees
from models.fees_historic_model import Fees_Historic
from models.fees_historic_individual import Fees_Historic_Individual

fees_routes = Blueprint('fees', __name__)

@fees_routes.route('/fees', methods = ['GET', 'POST'])
def fees():
    fees = Fees.get_fees_data()
    fees_historic_plot = Fees_Historic.get_fees_historic_line_plot()
    fees_by_type = Fees.get_fees_by_type_plot()
    fees_by_category = Fees.get_fees_by_category_plot()
    return render_template('fees.html', fees=fees, fees_historic_plot = fees_historic_plot,
                           fees_by_type = fees_by_type, fees_by_category = fees_by_category )


@fees_routes.route( '/<string:name>', methods = ['GET'] )
def fees_individual( name ):
    data = Fees.get_individual_fees_data( name )
    name_for_historic = name.replace(' ', '_' ).lower()
    print( name_for_historic )
    Ind_fees = Fees_Historic_Individual( name_for_historic )
    fees_plot = Ind_fees.get_fees_line_chart()
    historic_data = Ind_fees.get_data()
    return render_template( 'fees_individual.html',  fee = data, 
                           fees_plot = fees_plot, historic_data = historic_data
                           )
    