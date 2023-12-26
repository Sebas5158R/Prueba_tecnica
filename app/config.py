class Config:
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:200530@localhost/credifamilia'

    SQLALCHEMY_TRACK_MODIFICATION=False
    
    # Para encriptar los envios de formularios
    SECRET_KEY = 'PROJECTOCREDIFAMILIASECRETKEY'