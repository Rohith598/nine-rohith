from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def read():
    return "welcome to fastapi"

@app.get("/name")
def get_name():
    return "rohith-developer"
