# Scenario: You're a developer at an AI-powered bouquet design company. 
# Your clients can describe their dream bouquet, and your system generates 
# realistic images for their approval. To further enhance the experience, 
# you're integrating cutting-edge image analysis to provide descriptive 
# summaries of the generated bouquets. Your main application will invoke 
# the relevant methods based on the users' interaction and to facilitate that,
# you need to finish the below tasks:

# Task 1: Develop a Python function named generate_bouquet_image(prompt). 
# This function should invoke the imagen-3.0-generate-002 model using 
# the supplied prompt, generate the image, and store it locally. 
# For this challenge, use the prompt: Create an image containing 
# a bouquet of 2 sunflowers and 3 roses.

# The answer:

import argparse

import vertexai
from vertexai.preview.vision_models import ImageGenerationModel


def generate_image(
    project_id: str,
    location: str,
    output_file: str,
    prompt: str,
) -> vertexai.preview.vision_models.ImageGenerationResponse:
    """Generate an image using a text prompt.

    Args:
        project_id: Google Cloud project ID, used to initialize Vertex AI.
        location: Google Cloud region, used to initialize Vertex AI.
        output_file: Local path to the output image file.
        prompt: The text prompt describing what you want to see.
    """

    vertexai.init(project=project_id, location=location)

    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")

    images = model.generate_images(
        prompt=prompt,
        # Optional parameters
        number_of_images=1,
        seed=1,
        add_watermark=False,
    )

    images[0].save(location=output_file)

    return images


generate_image(
    project_id="[YOUR_PROJECT_ID]",
    location="[YOUR_PROJECT_LOCATION]",
    output_file="image.jpeg",
    prompt="Create an image containing a bouquet of 2 sunflowers and 3 roses",
)
