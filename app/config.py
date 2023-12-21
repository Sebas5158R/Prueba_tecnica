class Config:
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:@localhost/credifamilia'

    SQLALCHEMY_TRACK_MODIFICATION=False
    
    # Para encriptar los envios de formularios
    SECRET_KEY = 'PROJECTOCREDIFAMILIASECRETKEY'