# models/tvl_historic_model.py

from app import db
from datetime import datetime
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio

class Tvl_historic(db.Model):
    __tablename__ = 'historic'
    __bind_key__ = 'protocols_tvl'
    date = db.Column( db.DateTime, primary_key = True )
    tvl = db.Column( db.Float )
    _1d_change = db.Column(db.Float, name='1d_change')  
    _7d_change = db.Column(db.Float, name='7d_change')  
    _30d_change = db.Column(db.Float, name='30d_change')  
    _90d_change = db.Column(db.Float, name='90d_change')  
    _180d_change = db.Column(db.Float, name='180d_change')  
    _1y_change = db.Column(db.Float, name='1y_change') 

    def __repr__( self ):
        return f"<Tvl at: { self.date } is ({ self.tvl })>"
    
    @staticmethod
    def get_tvl_historic_data():
        tvl_data = Tvl_historic.query.all()
        return tvl_data
    
    
    @staticmethod
    def get_tvl_x_day(day):
        data = Tvl_historic.query.filter_by(date=day).first()
        if data:
            return data
        else:
            return Tvl_historic.query.order_by(Tvl_historic.date.desc()).first()


    @staticmethod
    def get_tvl_line_chart():
        tvl_data = Tvl_historic.query.all()

        # Extracting data for the plot
        dates = [entry.date for entry in tvl_data]
        tvls = [entry.tvl for entry in tvl_data]

        # Create a subplot with two y-axes
        fig = make_subplots(specs=[[{"secondary_y": False}]])

        # Plot TVL on the primary y-axis
        fig.add_trace(go.Scatter(x=dates, y=tvls, mode='lines', name='TVL',
                                 line=dict(color='#42B2D7'), showlegend=False), secondary_y=False)

        # Update layout
        fig.update_layout(
            title='Total Value Locked (TVL) Over Time',
            xaxis_title='Date',
            yaxis_title='TVL',
            plot_bgcolor='#091E42',
            paper_bgcolor='#091E42',
            xaxis=dict(linecolor='black', linewidth=4, showgrid=False, gridcolor='#161A1D'),
            yaxis=dict(linecolor='black', linewidth=4, showgrid=True, gridcolor='#E9F2FF'),
            font=dict(family="Calibri, sans-serif", size=16, color="#E9F2FF")  # Font style
        )

        # Convert the plot to HTML
        plot_html = pio.to_html(fig, full_html=False)

        return plot_html