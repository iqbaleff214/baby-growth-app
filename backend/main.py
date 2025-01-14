from fastapi import FastAPI

app = FastAPI(title="Baby Growth API", description="API untuk POC Baby Growth App", version="0.0.0")

@app.get("/")
async def root():
    return {"message": "Halo, duniaku!"}
