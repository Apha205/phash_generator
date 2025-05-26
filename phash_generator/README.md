# phashgenerator

phashgenerator is a simple Python utility to calculate the perceptual hash (pHash) of a video or image file.

## Installation

You can install it using pip:
```bash
pip install phashgenerator

Usage
from phashgenerator import calculate_phash
phash = calculate_phash("path/to/your/image_or_video.jpg")
print(phash)

What is pHash?
A perceptual hash is a fingerprint of a file based on its visual content. Similar images or videos will have similar hashes, even if they are resized or compressed.