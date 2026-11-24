"""Step 8 - Generate an image with an open-source image model (FLUX)."""
import base64

from together import Together

from common import require_key

require_key()
client = Together()

r = client.images.generate(
    model="black-forest-labs/FLUX.1-schnell",
    prompt="A cozy roadside chai stall at sunset, watercolor style",
    width=1024,
    height=768,
    steps=4,
    response_format="base64",
)

with open("chai_stall.png", "wb") as f:
    f.write(base64.b64decode(r.data[0].b64_json))
print("Saved chai_stall.png")
