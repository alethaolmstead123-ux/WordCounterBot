import os

# Get bot token from environment variable (Railway) or fallback
BOT_TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

# Check if token is set
if BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
    print("⚠️ WARNING: Using default bot token. Please set BOT_TOKEN environment variable!")
