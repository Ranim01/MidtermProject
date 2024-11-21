from fastapi import FastAPI
 
app=FastAPI()

@app.get("/")
def read_route():
    return{"message":"Hello, FastAPI"}

@app.get("/message/{name}/{grade}")
def greet(name: str, grade: int):     
    greeting_message = f"{name}"         
    if grade < 10:         
        return {"message": greeting_message, "Result": "You have failed"}
    else:         
        return {"message": greeting_message, "Result": "You have passed the exam."} 
@app.get("/multiply")
def multiply_numbers(x: int, y: int):     
    result = x * y     
    return {"result": result, "operation": f"{x} multiplied by {y}"}
    
#