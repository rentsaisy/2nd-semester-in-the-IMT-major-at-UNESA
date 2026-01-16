# Task 2: Develop a second Python function called analyze_bouquet_image(image_path).
# This function will take the image path as input along with a text prompt to 
# generate birthday wishes based on the image passed and send it to the model-id model. 
# To ensure responses can be obtained as and when they are generated, enable streaming 
# on the prompt requests.

# The answer:

import vertexai
from vertexai.generative_models import GenerativeModel, Part, Image, Content

def analyze_bouquet_image(project_id: str, location: str):
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)

    # Load the Gemini multimodal model (version 2.0 flash)
    model = GenerativeModel("gemini-2.0-flash-001")

    # Load the image from file
    image_path = "/home/student/image.jpeg"  # Update if your path is different
    image_part = Part.from_image(Image.load_from_file(image_path))

    # Ask initial question about image content
    print("📷 Image Analysis: ", end="", flush=True)
    response_stream = model.generate_content(
        [image_part, Part.from_text("Generate birthday wishes based on this image")],
        stream=True
    )

    full_response = ""
    for chunk in response_stream:
        if chunk.text:
            print(chunk.text, end="", flush=True)
            full_response += chunk.text
    print("\n")


# Set your project and location
project_id = "[YOUR_PROJECT_ID]"
location = "[YOUR_PROJECT_LOCATION]"

# Run the function
analyze_bouquet_image(project_id, location)