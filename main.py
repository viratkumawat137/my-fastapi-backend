from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

app = FastAPI()
              
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database aur Table create karne ka function
def init_db():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Server start hote hi database initialize ho jayega
init_db()

class ContactData(BaseModel):
    name: str
    email: str
    message: str

@app.post("/api/contact")
async def receive_contact(data: ContactData):
    # Database mein data save karna
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
        (data.name, data.email, data.message)
    )
    conn.commit()
    conn.close()

    print("--- Naya Message Database Mein Save Ho Gaya ---")
    print(f"Name: {data.name}, Email: {data.email},Message: {data.message}")
    return {
        "status": "success",
        "message": "Data successfully saved in SQLite database!"
    }
