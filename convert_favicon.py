import sys
from PIL import Image

input_path = "C:\\Users\\niels\\.gemini\\antigravity\\brain\\386d8fa7-f3b5-4a9b-9eb1-858e8300e37d\\media__1772657063034.jpg"
output_path = "d:\\Projects\\site\\filteredCode\\favicon.ico"

try:
    img = Image.open(input_path)
    img = img.resize((256, 256), Image.Resampling.LANCZOS)
    img.save(output_path, format='ICO', sizes=[(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)])
    print("Favicon saved successfully.")
except Exception as e:
    print(f"Error: {e}")
