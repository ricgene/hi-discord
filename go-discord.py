import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID', 123456789012345678))  # Replace with your channel ID

# Validate environment variables
if not BOT_TOKEN or BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
    raise ValueError("Please set your Discord bot token in the .env file")

# Create bot instance
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
    # Get the channel
    channel = bot.get_channel(CHANNEL_ID)
    
    if channel:
        # Send your message
        message = "Hello from Python! This is an automated message."
        await channel.send(message)
        print(f"Message sent to #{channel.name}")
    else:
        print("Channel not found!")
    
    # Close the bot after sending the message
    await bot.close()

# Alternative function-based approach without bot commands
async def send_message():
    # Create client
    client = discord.Client(intents=discord.Intents.default())
    
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        
        # Get the channel
        channel = client.get_channel(CHANNEL_ID)
        
        if channel:
            # Send your message
            message = "Hello from Python! This is an automated message."
            await channel.send(message)
            print(f"Message sent to #{channel.name}")
        else:
            print("Channel not found!")
        
        # Close the client after sending the message
        await client.close()
    
    # Run the client
    await client.start(BOT_TOKEN)

# Run the bot
if __name__ == "__main__":
    # Method 1: Using bot
    asyncio.run(bot.start(BOT_TOKEN))
    
    # Method 2: Using client (uncomment to use instead)
    # asyncio.run(send_message())