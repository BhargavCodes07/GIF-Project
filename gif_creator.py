from PIL import Image, ImageDraw

# Image size
width = 300
height = 300

frames = []

# Create animation frames
for i in range(30):
    # Create blank image
    image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(image)

    # Moving circle position
    x = 10 + (i * 8)
    y = 130

    # Draw circle
    draw.ellipse((x, y, x + 50, y + 50), fill="red")

    # Save frame
    frames.append(image)

# Save as GIF
frames[0].save(
    "moving_ball.gif",
    save_all=True,
    append_images=frames[1:],
    duration=80,
    loop=0
)

print("GIF created successfully!")