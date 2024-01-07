import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import pandas as pd
from app import db

class Volume(db.Model):
    __tablename__ = 'dex_volume_general'
    __bind_key__ = 'volume'
    
    defillamaId = db.Column(db.Integer, primary_key=True )
    name = db.Column(db.String)
    disabled = db.Column(db.Integer)
    display_name = db.Column(db.String, name='displayName')
    module = db.Column(db.String)
    category = db.Column(db.String)
    logo = db.Column(db.String)
    change_1d = db.Column(db.Float)
    change_7d = db.Column(db.Float)
    change_1m = db.Column(db.Float)
    change_7dover7d = db.Column(db.Float)
    change_30dover30d = db.Column(db.Float)
    total24h = db.Column(db.Float)
    total48hto24h = db.Column(db.Float)
    total7d = db.Column(db.Float)
    total30d = db.Column(db.Float)
    total14dto7d = db.Column(db.Float)
    total60dto30d = db.Column(db.Float)
    total_all_time = db.Column(db.Float, name = 'totalAllTime')
    methodologyUrl = db.Column(db.String)
    versionKey = db.Column(db.String)
    dailyVolume = db.Column(db.Float)
    parentProtocol = db.Column(db.String)
    
    def __repr__(self):
        return f"<Volume {self.name} - ID: {self.defillama_id}>"
    
    
    @staticmethod
    def get_volume_data():
        data = Volume.query.order_by( Volume.dailyVolume.desc() ).limit( 100 ).all()
        return data
    
    @staticmethod
    def get_dex_by_name(name):
        dex = Volume.query.filter_by(name=name).first()
        return dex

    @staticmethod
    def get_dex_by_volume_greater_than(volume_threshold):
        dex_list = Volume.query.filter(Volume.daily_volume > volume_threshold).all()
        return dex_list

    @staticmethod
    def get_top_x_dex_by_volume(x):
        top_dex_list = Volume.query.order_by(Volume.daily_volume.desc()).limit(x).all()
        return top_dex_list

    @staticmethod
    def get_bottom_x_dex_by_volume(x):
        bottom_dex_list = Volume.query.order_by(Volume.daily_volume).limit(x).all()
        return bottom_dex_list

    @staticmethod
    def get_top_x_dex_by_volume_change(x, time_period):
        time_column = f"change_{time_period.lower().replace(' ', '_')}"
        top_dex_list = Volume.query.order_by(getattr(Volume, time_column).desc()).limit(x).all()
        return top_dex_list

    @staticmethod
    def get_bottom_x_dex_by_volume_change(x, time_period):
        time_column = f"change_{time_period.lower().replace(' ', '_')}"
        bottom_dex_list = Volume.query.order_by(getattr(Volume, time_column)).limit(x).all()
        return bottom_dex_list

    @staticmethod
    def group_volume_by_categories():
        grouped_data = db.session.query(Volume.category, db.func.sum(Volume.daily_volume)).group_by(Volume.category).all()
        return grouped_data
    
    
    def get_volume_line_chart():
    # Query data from the Volume table
        data = db.session.query(
        Volume.category,
        db.func.sum(Volume.total24h).label('total24h'),
        db.func.count(Volume.name).label('protocol_count')
        ).group_by(Volume.category).all()

        # Convert the result to a DataFrame
        df = pd.DataFrame(data, columns=['Category', 'Total 24H', 'Protocol Count'])

        # Create a grouped bar chart using Plotly Express
        fig = go.Figure()
        fig.add_trace(go.Bar(x=df['Category'], y=df['Total 24H'], name='Total 24H', text=df['Total 24H']))
        fig.add_trace(go.Bar(x=df['Category'], y=df['Protocol Count'], name='Protocol Count', text=df['Protocol Count']))
        # Customize layout
        fig.update_layout(
            barmode='group',  # Grouped bar chart
            title_text='Total 24H and Protocol Count by Category',
            xaxis_title='Category',
            yaxis_title='Values',
            plot_bgcolor='#091E42',
            paper_bgcolor='#091E42',
            font=dict(family="Calibri, sans-serif", size=16, color="#E9F2FF"),
            showlegend = False
        )

        # Convert to HTML and return
        plot_html = pio.to_html(fig, full_html=False)
        return plot_html
    
    
    def get_volume_bar_chart_top25():
        data = db.session.query(Volume.name, Volume.total_all_time).order_by(Volume.total_all_time.desc()).limit(5).all()

        df = pd.DataFrame(data, columns=['Name', 'AthVolume'])

        fig = px.bar(df, x='Name', y='AthVolume', title='All time Volume', text = 'AthVolume' )

        fig.update_layout(
            xaxis_title='Name',
            yaxis_title='All time Volume',
            plot_bgcolor='#091E42',
            paper_bgcolor='#091E42',
            font=dict(family="Calibri, sans-serif", size=16, color="#E9F2FF")
        )

        # Convert to HTML and return
        plot_html = pio.to_html(fig, full_html=False)
        return plot_html
    
    
    def get_x_best_n_worst_performers_plot():
        b1 = Volume.get_top_x_dex_by_volume_change(5, '1d')
        b7 = Volume.get_top_x_dex_by_volume_change(5, '7d')
        b30 = Volume.get_top_x_dex_by_volume_change(5, '1m')
        
        w1 = Volume.get_bottom_x_dex_by_volume_change(5, '1d')
        w7 = Volume.get_bottom_x_dex_by_volume_change(5, '7d')
        w30 = Volume.get_bottom_x_dex_by_volume_change(5, '1m')
        
        # scatter plot
        bcolors = ['#BAF3DB', '#2ABB7F', '#1F845A' ]
        wcolors = ['#FFD5D2', '#F15B50', '#C9372C' ]
        
        best_df = pd.concat([pd.DataFrame(df, columns=['your_x_column', 'your_y_column']) for df in [b1, b7, b30]], keys=['1d', '7d', '1m'])
        worst_df = pd.concat([pd.DataFrame(df, columns=['your_x_column', 'your_y_column']) for df in [w1, w7, w30]], keys=['1d', '7d', '1m'])

        
        # Create scatter plot
        fig = px.scatter(
            best_df, x='total24h', y='name', color='level_0',
            title='Best Performers Scatter Plot',
            color_discrete_map={'1d': '#BAF3DB', '7d': '#2ABB7F', '1m': '#1F845A'}
        )

        # Customize layout
        fig.update_layout(
            xaxis_title='X Axis Title',
            yaxis_title='Y Axis Title',
            plot_bgcolor='#091E42',
            paper_bgcolor='#091E42',
            font=dict(family="Calibri, sans-serif", size=16, color="#E9F2FF")
        )

        # Convert to HTML and return
        plot_html = pio.to_html(fig, full_html=False)
        return plot_html

        