from app import db

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

class Volume_Historic(db.Model):
    __tablename__ = 'dex_volumes_historic'
    __bind_key__ = 'volume'
    
    date = db.Column(db.DateTime, primary_key=True)
    volume = db.Column(db.Float)
    _1d_change = db.Column(db.Float, name='1d_change')  
    _7d_change = db.Column(db.Float, name='7d_change')  
    _30d_change = db.Column(db.Float, name='30d_change')  
    _90d_change = db.Column(db.Float, name='90d_change')  
    _180d_change = db.Column(db.Float, name='180d_change')  
    _1y_change = db.Column(db.Float, name='1y_change')  
    cumulative_volume = db.Column(db.Float)
    
    def __repr__(self):
        return f"<Day: {self.date} Volume - ({self.volume})>"

    @staticmethod
    def get_volume_historic_data():
        vol_data = Volume_Historic.query.all()
        return vol_data
    
    @staticmethod
    def get_volume_x_day(day):
        data = Volume_Historic.query.filter_by(date=day).first()
        if data:
            return data
        else:
            return Volume_Historic.query.order_by(Volume_Historic.date.desc()).first()
        
        
    @staticmethod
    def get_volume_line_chart():
        vol_data = Volume_Historic.query.all()

        dates = [entry.date for entry in vol_data]
        volumes = [entry.volume for entry in vol_data]
        cumulative_volumes = [entry.cumulative_volume for entry in vol_data]

        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.add_trace(go.Scatter(x=dates, y=volumes, mode='lines', name='Volume', 
                                 line=dict(color='#388BFF'), showlegend=False), secondary_y=False)

        fig.add_trace(go.Scatter(x=dates, y=cumulative_volumes, mode='lines', name='Cumulative Volume', 
                                 line=dict(color='#DA62AC'), showlegend=False), secondary_y=True)

        fig.update_layout(
            title='Volume Over Time',
            xaxis_title='Date',
            yaxis_title='Daily Volume',
            yaxis2_title='Cumulative Volume',
            plot_bgcolor='#091E42', 
            paper_bgcolor='#091E42',
            xaxis=dict(linecolor='black', linewidth=4, showgrid=False, gridcolor='#161A1D' ), 
            yaxis=dict(linecolor='black', linewidth=4, showgrid=True, gridcolor='#E9F2FF' ), 
            yaxis2=dict(linecolor='black', linewidth=4, showgrid=True, gridcolor='#161A1D' ),  
            xaxis2=dict(linecolor='black', linewidth=4, showgrid=False, gridcolor='#161A1D' ),  
            font=dict(family="Calibri, sans-serif", size=16, color="#E9F2FF")  # Font style
        )

        # Convert the plot to HTML
        plot_html = pio.to_html(fig, full_html=False)

        return plot_html
    
    
    
