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
    