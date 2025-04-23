from sqlmodel import create_engine, Session, SQLModel

local_mariadb = "mysql+pymysql"
engine = create_engine('{db}://{username}:{password}@{host}:{port}/{db_name}'.format(
    db=local_mariadb,
    username='kong',
    password='1234',
    host='localhost',
    port='3306',
    db_name='kong'
), echo=False)  # echo= sql log
# engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session


def init_db():
    SQLModel.metadata.create_all(engine)
