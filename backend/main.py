from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from io import BytesIO
from PIL import Image, ImageDraw
import requests
import os

app = FastAPI(title="Baby Growth API", description="API untuk POC Baby Growth App", version="0.0.0")

# Allow all origins (for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

if 'STABILITY_AI_KEY' not in os.environ:
    print('You need to set env variable')
    exit(0)

@app.get("/")
async def root():
    return {"message": "Halo, duniaku!"}

@app.post("/v1/process-image/")
async def process_image(father: UploadFile = File(...), mother: UploadFile = File(...)):
    try:
        secret_key = os.getenv('STABILITY_AI_KEY')

        # Read the uploaded image file
        contents = await father.read()

        # Request AI generation
        response = requests.post(
            f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
            headers={
                "authorization": f"Bearer {secret_key}",
                "accept": "image/*"
            },
            files={
                "image": ("filename.jpg", contents, "image/jpeg")
            },
            data={
                "prompt": "Generate a prediction of this person's child at age 1",
                "output_format": "jpeg",
                "mode": "image-to-image",
                "model": "sd3-medium",
                "strength": 0.8
            },
        )

        if response.status_code != 200:
            raise Exception(str(response.json()))

        input_image = Image.open(BytesIO(response.content))

        # Process the image to add a watermark or other transformation
        output_image = input_image.copy()
        draw = ImageDraw.Draw(output_image)
        draw.text((10, 10), "Watermark", fill="white")  # Add a simple text watermark

        # Save the processed image to a BytesIO buffer
        buffer = BytesIO()
        output_image.save(buffer, format="JPEG")
        buffer.seek(0)

        # Return the processed image
        return StreamingResponse(buffer, media_type="image/jpeg")
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"message": e}
