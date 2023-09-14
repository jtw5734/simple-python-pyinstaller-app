
import uvicorn

if __name__ == "__main__":
    uvicorn.run( "app:app" ,host="0.0.0.0", port=13000,  reload=False, workers=5) 