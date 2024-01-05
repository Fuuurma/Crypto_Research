import plotly.express as px
import plotly.io as pio
from app import db

class Fees_Historic(db.Model):
    __tablename__ = 'historic'
    __bind_key__ = 'fees'
    
    date = db.Column( db.DateTime, primary_key=True )
    fees = db.Column( db.Float )
    _1d_change = db.Column( db.Float, name = '1d_change' )
    _7d_change = db.Column( db.Float,name = '7d_change' )
    _30d_change = db.Column( db.Float, name = '30d_change' )
    _90d_change = db.Column( db.Float, name = '90d_change' )
    _180d_change = db.Column( db.Float, name = '180d_change' )
    _1y_change = db.Column( db.Float, name = '1y_change' )
    rolling_mean_10 = db.Column( db.Float )
    rolling_mean_25 = db.Column( db.Float )
    rolling_mean_50 = db.Column( db.Float )
    rolling_mean_100 = db.Column( db.Float )
    rolling_std_10 = db.Column( db.Float )
    rolling_std_25 = db.Column( db.Float )
    rolling_std_50 = db.Column( db.Float )
    rolling_std_100 = db.Column( db.Float )
    rolling_min_10 = db.Column( db.Float )
    rolling_min_25 = db.Column( db.Float )
    rolling_min_50 = db.Column( db.Float )
    rolling_min_100 = db.Column( db.Float )
    rolling_max_10 = db.Column( db.Float )
    rolling_max_25 = db.Column( db.Float )
    rolling_max_50 = db.Column( db.Float )
    rolling_max_100 = db.Column( db.Float )
    historical_volatility = db.Column( db.Float )
    ema_12 = db.Column( db.Float )
    ema_26 = db.Column( db.Float )
    macd = db.Column( db.Float )
    signal_line = db.Column( db.Float )
    rsi = db.Column( db.Float )
    rate_of_change = db.Column( db.Float )
    momentum = db.Column( db.Float )
    sma_20 = db.Column( db.Float )
    upper_band = db.Column( db.Float )
    lower_band = db.Column( db.Float )
    stoch_oscillator = db.Column( db.Float )

    def __repr__(self):
        return f"<Fees_Historic { self.date } - { self.fees }>"
    
    @staticmethod
    def get_fees_historic_line_plot():
        # Assuming 'Fees_Historic' is the model for historic fees data
        historic_data = Fees_Historic.query.order_by(Fees_Historic.date).all()

        if not historic_data:
            return None  # Return None if no data is available

        # Extract data for plotting
        dates = [entry.date for entry in historic_data]
        fees = [entry.fees for entry in historic_data]

        # Create line plot using Plotly Express
        fig = px.line(x=dates, y=fees, labels={'x': 'Date', 'y': 'Fees'}, title='Historic Fees Line Plot')

        # Customize layout
        fig.update_layout(
            plot_bgcolor='#091E42',
            paper_bgcolor='#091E42',
            font=dict(family="Calibri, sans-serif", size=16, color="#E9F2FF")
        )

        plot_html = pio.to_html(fig, full_html=False)
        return plot_html
