from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from io import BytesIO
from PIL import Image, ImageDraw

app = FastAPI(title="Baby Growth API", description="API untuk POC Baby Growth App", version="0.0.0")

# Allow all origins (for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
    return {"message": "Halo, duniaku!"}

@app.post("/v1/process-image/")
async def process_image(father: UploadFile = File(...), mother: UploadFile = File(...)):
    try:
        # Read the uploaded image file
        contents = await mother.read()
        input_image = Image.open(BytesIO(contents))

        # Process the image (example: add a watermark or other transformation)
        output_image = input_image.copy()
        draw = ImageDraw.Draw(output_image)
        draw.text((10, 10), "Watermark", fill="red")  # Add a simple text watermark

        # Save the processed image to a BytesIO buffer
        buffer = BytesIO()
        output_image.save(buffer, format="JPEG")
        buffer.seek(0)

        # Return the processed image
        return StreamingResponse(buffer, media_type="image/jpeg")
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"message": e}
