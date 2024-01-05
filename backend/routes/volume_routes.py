from flask import Blueprint, render_template
from app import db
from models.volume_historic_model import Volume_Historic
from models.volume_model import Volume

volume_routes = Blueprint( 'volume', __name__ )

@volume_routes.route( '/', methods = [ 'GET', 'POST' ] )
def volume():
    historic_volume = Volume_Historic.get_volume_historic_data()
    volume_historic_plot = Volume_Historic.get_volume_line_chart()
    
    volume_general = Volume.get_volume_data()
    
    all_time_plot = Volume.get_volume_bar_chart_top25()
    categories_plot = Volume.get_volume_line_chart()
    # xxx = Volume.get_x_best_n_worst_performers_plot()
    return render_template( 'volume.html', historic_volume = historic_volume, volume_historic_plot = volume_historic_plot,
                           volume_general = volume_general, all_time_plot = all_time_plot, categories_plot = categories_plot,
                        #    xxx = xxx
                           )