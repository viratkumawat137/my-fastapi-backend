from sqlmodel import SQLModel, Field, create_engine, Session,select

class Laptop(SQLModel,  table=True):
    id: int = Field(default=None, primary_key=True)
    model:str =Field (min_length=3,max_length=20)
    num_of_key:int
    usb_port:int
    power_supp:int


conn = create_engine("sqlite:///18-nov.db")

SQLModel.metadata.create_all(conn)


db=Session(conn)


# dummy_laptops = [
#     Laptop(model="Dell Latitude 5310", num_of_key=80, usb_port=2, power_supp=65),
#     Laptop(model="HP Pavilion 15", num_of_key=104, usb_port=3, power_supp=65),
#     Laptop(model="Lenovo ThinkPad T14", num_of_key=84, usb_port=2, power_supp=65),
#     Laptop(model="MacBook Air M2", num_of_key=78, usb_port=0, power_supp=30),
#     Laptop(model="Asus ROG Strix", num_of_key=98, usb_port=4, power_supp=240),
#     Laptop(model="Acer Aspire 5", num_of_key=99, usb_port=3, power_supp=45),
# ]


# for x in dummy_laptops:
#     db.add(x)


#  aditional data ko db mee add krna 
# a = Laptop(model="dell z34", num_of_key=84, usb_port=43, power_supp=65)
# db.add(a)


# query=select(Laptop).filter(Laptop.power_supp==65)


# result=db.exec(query).all()
# result=db.exec(query).first()
# result=db.exec(query).all()
# result=db.exec(query).one()


#delet krna data ko 


# print(result.power_supp)
# print(type(result))


query=select(Laptop).filter(Laptop.id==2)
result=db.exec(query).first()
db.delete(result)
db.commit()
print(result)



