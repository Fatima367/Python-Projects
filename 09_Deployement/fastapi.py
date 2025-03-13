from fastapi import FastAPI

# Created a fastAPI application instance
app = FastAPI()

# Defining get endpoint at the route '/hello'
@app.get("/hello")
def hello_world():
    # Return a simple string response
    return {"message" : "Hello World!"}