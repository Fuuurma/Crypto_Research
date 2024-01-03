# routes/tvl_routes.py

from flask import Blueprint, render_template, url_for
from models.tvl_historic_model import Tvl_historic
from models.protocol_model import Protocol
from models.chain_model import Chain

tvl_routes = Blueprint('tvl', __name__)

@tvl_routes.route('/historic', methods = ['GET', 'POST'])
def tvl_historic():
    tvl_historic_data = Tvl_historic.query.limit(10).all()
    tvl_plot = Tvl_historic.get_tvl_line_chart()
    return render_template('tvl_historic.html', tvl_historic=tvl_historic_data, tvl_plot = tvl_plot)

@tvl_routes.route('/', methods = ['GET', 'POST'])
def tvl():
    tvl_table = Protocol.get_protocols_data()
    actual_tvl = Protocol.get_actual_TVL()
    number_of_protocols = Protocol.get_number_of_protocols()
    tvl_plot = Tvl_historic.get_tvl_line_chart()
    
    
    chain_table = Chain.get_chains_data()
    
    return render_template('tvl.html', tvl_table = tvl_table, actual_tvl= actual_tvl, number_of_protocols = number_of_protocols,
                           chain_table = chain_table, tvl_plot = tvl_plot )


@tvl_routes.route('/protocols', methods = ['GET', 'POST'])
def protocols():
    tvl_table = Protocol.get_protocols_data()
    return render_template('protocols.html', tvl_table = tvl_table )

@tvl_routes.route('/protocols/<int:id>', methods=['GET', 'POST'])
def protocol(id):
    protocol_data = Protocol.search_protocols_by_id(id)
    return render_template('protocol.html', protocol_data=protocol_data)


@tvl_routes.route('/chains', methods = ['GET', 'POST'])
def chains():
    chains_data = Chain.get_chains_data()
    return render_template('chains.html', chains_data = chains_data )

@tvl_routes.route('/chains/<string:id>', methods=['GET', 'POST'])
def chain(id):
    chain_data = Chain.get_chain_data(id)
    return render_template('chain.html', chain_data=chain_data)