class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://usr_calidad_rrss:YryJimADb68NK5Xb@144.22.138.159/db_calidad_rrss'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://db_test_calidad_rrss:hJFibzXyjBN27tDs@144.22.138.159/db_test_calidad_rrss'
