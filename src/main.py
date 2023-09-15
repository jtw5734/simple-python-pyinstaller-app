
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "v1.0.8"}




if __name__ == "__main__":
    uvicorn.run( app ,host="0.0.0.0", port=13000, reload=False) 