# models/fees_model.py
import plotly.graph_objects as go
import plotly.io as pio

from app import db

class Fees(db.Model):
    __tablename__ = 'general'
    __bind_key__ = 'fees'
    defillamaId = db.Column( db.Integer , primary_key=True)
    name = db.Column( db.String( 255 ))
    disabled = db.Column( db.String( 1)) 
    displayName = db.Column( db.String( 255 ))
    module = db.Column( db.String( 255 ))
    category = db.Column( db.String( 255 ))
    logo = db.Column( db.String( 255 ))
    change_1d = db.Column( db.Float )
    change_7d = db.Column( db.Float )
    change_1m = db.Column( db.Float )
    change_7dover7d = db.Column( db.Float )
    change_30dover30d = db.Column( db.Float )
    total24h = db.Column( db.Float )
    total48hto24h = db.Column( db.Float )
    total7d = db.Column( db.Float )
    total30d = db.Column( db.Float )
    total14dto7d = db.Column( db.Float )
    total60dto30d = db.Column( db.Float )
    totalAllTime = db.Column( db.Float )
    protocolType = db.Column( db.String( 255 ))
    methodologyURL = db.Column( db.String( 255 ))
    parentProtocol = db.Column( db.String( 255 ))
    latestFetchIsOk = db.Column( db.String( 1 )) 
    versionKey = db.Column( db.String( 255 ))
    dailyRevenue = db.Column( db.Float )
    dailyUserFees = db.Column( db.Float )
    dailyHoldersRevenue = db.Column( db.Float )
    dailyCreatorRevenue = db.Column( db.Float )
    dailySupplySideRevenue = db.Column( db.Float )
    dailyProtocolRevenue = db.Column( db.Float )
    dailyBribesRevenue = db.Column( db.Float )
    dailyFees = db.Column( db.Float )
    holdersRevenue30d = db.Column( db.Float )

    def __repr__(self):
        return f"<Fees {self.name}>"
    
    @staticmethod
    def get_fees_data():
        fees = Fees.query.limit( 100 ).all()
        return fees


    @staticmethod
    def get_fees_pie_chart( top = 10, other_fees = True ):
        data = Fees.query.order_by( Fees.total24h ).limit( top ).all()
        
        labels = [ fee.name for fee in data ]
        values = [ fee.total24h for fee in data ]
        
        if other_fees:
            other_data = Fees.query.order_by( Fees.total24h.desc() ).offset( top ).all()
            if other_data:
                labels.append( "Other protocol fees" )
                values.append(sum([fee.total24h if fee.total24h is not None else 0 for fee in other_data]))
                
        fig = go.Figure( data = [ go.Pie( labels = labels, values = values )])
        fig.update_layout(
            title = "Fees",
            plot_bgcolor='#091E42',
            paper_bgcolor='#091E42',
            font=dict(family="Calibri, sans-serif", size=16, color="#E9F2FF")
        )
        plot_html = pio.to_html( fig, full_html = False )
        return plot_html
            
            