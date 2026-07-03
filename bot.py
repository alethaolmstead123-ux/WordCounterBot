from commands import bot
import os
import time
import sys

if __name__ == "__main__":
    print("🤖 WordCounterBot is starting...")
    
    try:
        bot_info = bot.get_me()
        print(f"✅ Bot is running! Username: @{bot_info.username}")
        print("✅ Waiting for messages...")
        
        # Remove webhook if set (prevents 409 errors)
        try:
            bot.remove_webhook()
            print("✅ Webhook removed")
        except:
            pass
        
        # Start polling with error handling
        while True:
            try:
                bot.infinity_polling(timeout=60, long_polling_timeout=30)
            except Exception as e:
                print(f"⚠️ Polling error: {e}")
                print("🔄 Restarting polling in 5 seconds...")
                time.sleep(5)
                
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)
