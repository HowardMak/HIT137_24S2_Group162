import PIL.Image as Image
import time

# Get the number
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10

# Load the original image and modify pixels
img = Image.open("chapter1.jpg")
pixels = img.load()
width, height = img.size
#shift the pixels
for m in range(width):
    for n in range(height):
        r, g, b = pixels[m, n]
        new_red = min(255, r + generated_number) #red pixels
        new_green = min(255, g + generated_number) #green pixels
        new_blue = min(255, b + generated_number) # blue pixels
        pixels[m, n] = (new_red, new_green, new_blue)

# Save the new image
img.save("chapter1out.jpg")

# Calculate sum of red pixel values
red_sum = 0
for x in range(width):
    for y in range(height):
        r, _, _ = pixels[x, y]
        red_sum += r

print("Red Pixel Value of the Image: ", red_sum) #print the red pixel value
