import discord
from discord.ext import commands, tasks
import csv
from PIL import Image, ImageDraw, ImageFont
import datetime

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)

# Function to draw text onto an image at specified coordinates with formatting
def draw_text(image, text, coordinates, font_path, font_size, fill_color, bold=False):
    draw = ImageDraw.Draw(image)
    if bold:
        font = ImageFont.truetype(font_path, font_size, encoding="unic")
    else:
        font = ImageFont.truetype(font_path, font_size)
    draw.text(coordinates, text, fill=fill_color, font=font)

@bot.command()
async def scoreboard(ctx):
    await ctx.purge()
    csv_file = 'template.csv'
    coordinates_file = 'template_coordinates.csv'
    image_path = 'template_image.jpg'
    font_path = 'template_font.ttf'
    font_size = 36
    
    image = Image.open(image_path)
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        
        for idx, row in enumerate(reader):
            name = row['name']
            class_name = row['class']  # Extract the class name from the row
            
            # Open the coordinates CSV file and read its contents
            with open(coordinates_file, 'r') as coord_file:
                coord_reader = csv.reader(coord_file)
                # Read the coordinates corresponding to the current index
                coordinates = list(coord_reader)[idx]
                
            draw_text(image, f"{name}\n{class_name}", (int(coordinates[0]), int(coordinates[1])), font_path, font_size, fill_color=(0, 0, 0), bold=True)
    
    output_image_path = 'output_image.jpeg'
    image.save(output_image_path)
    
    # Send text message with the current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f"Last update was: {current_time}")
    
    # Send the image file
    await ctx.send(file=discord.File(output_image_path))

# Background task to send the image and message every one hour
@tasks.loop(hours=1)
async def send_image_and_message():
    # Get the channel where you want to send the message and image
    channel = bot.get_channel(CHANNEL_ID)  # Replace CHANNEL_ID with the actual channel ID
    
    csv_file = 'template.csv'
    class_names = {}  # Dictionary to store class names
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            class_names[row['name']] = row['class']  # Populate class_names dictionary
    
    # Clear the channel before sending
    await channel.purge()
    # Send the image file
    await channel.send(file=discord.File('output_image.jpeg'))
     # Send text message with the current date and time and class name
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Last update was: {current_time}\n"
    await channel.send(message)
    


@bot.event
async def on_ready():
    # Start the background task when the bot is ready
    send_image_and_message.start()

# Replace 'YOUR_DISCORD_BOT_TOKEN' with your actual bot token
bot.run('YOUR_DISCORD_BOT_TOKEN')
