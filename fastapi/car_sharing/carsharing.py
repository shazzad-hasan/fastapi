from fastapi import FastAPI
import uvicorn

from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/date")
def date():
    return {'date': datetime.now()}

if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)