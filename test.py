from sqlmodel import SQLModel, Field, create_engine, Session

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(nullable=False, unique=True)
    password: str = Field(nullable=False)
    mail: str

CONNECTION = create_engine("sqlite:///16-nov.db")

tr_var = Session(CONNECTION)
SQLModel.metadata.create_all(CONNECTION)

a = User(username="test", password="te3st", mail="test2@example.com")
b = User(username="sahil", password="tes345t", mail="te21st@example.com")
c = User(username="viratpy", password="test", mail="test@example.com")


tr_var.add(a)
tr_var.add(b)
tr_var.add(c)


tr_var.commit()