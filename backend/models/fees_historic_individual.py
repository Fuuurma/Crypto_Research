import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
from sqlalchemy import MetaData, Table

from app import db


class Fees_Historic_Individual(db.Model):
    __bind_key__ = 'fees'
    __table_args__ = {'extend_existing': True}

    date = db.Column(db.DateTime, primary_key=True)
    id = db.Column(db.String(48))

    fees = db.Column(db.Float)
    _1d_change = db.Column(db.Float, name = "1d_change")
    _7d_change = db.Column(db.Float, name = "7d_change")
    _30d_change = db.Column(db.Float, name = "30d_change")
    _90d_change = db.Column(db.Float, name = "90d_change")
    _180d_change = db.Column(db.Float, name = "180d_change")
    _1y_change = db.Column(db.Float, name = "1y_change")
    ema_10 = db.Column(db.Float)
    ema_25 = db.Column(db.Float)
    ema_50 = db.Column(db.Float)
    ema_100 = db.Column(db.Float)
    rolling_std_10 = db.Column(db.Float)
    rolling_std_25 = db.Column(db.Float)
    rolling_std_50 = db.Column(db.Float)
    rolling_std_100 = db.Column(db.Float)
    rolling_min_10 = db.Column(db.Float)
    rolling_max_10 = db.Column(db.Float)
    rolling_min_25 = db.Column(db.Float)
    rolling_max_25 = db.Column(db.Float)
    rolling_min_50 = db.Column(db.Float)
    rolling_max_50 = db.Column(db.Float)
    rolling_min_100 = db.Column(db.Float)
    rolling_max_100 = db.Column(db.Float)
    historical_volatility = db.Column(db.Float)
    ema_12 = db.Column(db.Float)
    ema_26 = db.Column(db.Float)
    macd = db.Column(db.Float)
    signal_line = db.Column(db.Float)
    rsi = db.Column(db.Float)
    momentum = db.Column(db.Float)
    sma_20 = db.Column(db.Float)
    upper_band = db.Column(db.Float)
    lower_band = db.Column(db.Float)
    log_return = db.Column(db.Float)

    def __init__(self, name):
        Fees_Historic_Individual.__table__.name = f'{name}_historic'

    def __repr__(self):
        return f"<Day: {self.date} ID - {self.id} Fees - ({self.fees})>"
        
    @staticmethod
    def get_data():
        data = Fees_Historic_Individual.query.all()
        return data 
    
    @staticmethod
    def get_fees_line_chart():
        data = Fees_Historic_Individual.query.all()
        name_instance = Fees_Historic_Individual.query.first()  # Assuming you want the first entry's name
        name = name_instance.id if name_instance else 'Unknown'  # Replace 'Unknown' with a default name
        dates = [entry.date for entry in data]
        fees = [entry.fees for entry in data]

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=dates, y=fees, mode='lines', name='Fees', line=dict(color='#388BFF')))

        fig.update_layout(
            title='Fees Over Time for ' + name,
            xaxis_title='Date',
            yaxis_title='Fees',
            plot_bgcolor='#091E42',
            paper_bgcolor='#091E42',
            xaxis=dict(linecolor='black', linewidth=4, showgrid=False, gridcolor='#161A1D'),
            yaxis=dict(linecolor='black', linewidth=4, showgrid=True, gridcolor='#E9F2FF'),
            font=dict(family="Calibri, sans-serif", size=16, color="#E9F2FF")  # Font style
        )

        # Convert the plot to HTML
        plot_html = pio.to_html(fig, full_html=False)

        return plot_html