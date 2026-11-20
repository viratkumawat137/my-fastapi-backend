from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session, select

app = FastAPI()


class Food(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    price: int = Field(default=None)
    category: str = Field(default=None, index=True)


conn = create_engine("sqlite:///19-nov.db")

SQLModel.metadata.create_all(conn)
db = Session(conn)


@app.post("/items")
def create_item(name: str, price: int, category: str):
    item = Food(name=name, price=price, category=category)
    db.add(item)
    db.commit()
    db.refresh(item)

    return {
        "status": True,
        "message": "Item created successfully",
        "data": item
    }


@app.get("/all_items")
def items():
    return 
{
    "status": True,
    "message": "Items retrieved successfully",
    "data": db.exec(select(Food)).all()
}


@app.get("/all_veg_items")
def items():
    return {
        "status": True,
        "message": "Veg items retrieved successfully",
        "data": db.exec(select(Food).filter(Food.category =="veg")).all()
    }


@app.get("/all_no_veg_items")
def items():
    return {
        "status": True,
        "message": "Non-veg items retrieved successfully",
        "data": db.exec(select(Food).filter(Food.category == "non-veg")).all()
    }




@app.get("/select_items")
def items(id:int):
    return {
        "status": True,
        "message": "Item retrieved successfully",
        "data": db.exec(select(Food).filter(Food.id == id)).first()
    }

@app.patch("/update_item")
def update_item(id:int, new_prize:int ):
   item =db.exec(select(Food).filter(Food.id == id)).first()
   item.price = new_prize
   db.commit()
   db.refresh(item)
   return {
       "status": True,
       "message": "Item updated successfully",
       "data": item
   }

@app.delete("/delete_item")
def delete_item(id:int):
    item = db.exec(select(Food).filter(Food.id == id)).first()
    db.delete(item)
    db.commit()
    return {
        "status": True,
        "message": "Item deleted successfully"
    }