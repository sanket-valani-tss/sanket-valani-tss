from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import os

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "..", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=chrome_options)
username = "sanket-valani-tss"
current_year = datetime.now().year

try:
    current_year = 2024
    url = f"https://github.com/{username}?tab=overview&from={current_year}-01-01"
    print(f"Capturing data for year {current_year}...")
    driver.get(url)
    time.sleep(5)  # Wait for page to load

    # Find contribution section
    contribution_section = driver.find_element(By.CLASS_NAME, "js-yearly-contributions")
    position_relative_divs = contribution_section.find_elements(By.CLASS_NAME, "position-relative")
    if not position_relative_divs:
        raise Exception("No elements found with class 'position-relative'")
    contribution_graph = position_relative_divs[0]

    # Save contribution graph screenshot
    contrib_path = os.path.join(ASSETS_DIR, f"contribution_graph_{current_year}.png")
    if contribution_graph.screenshot(contrib_path):
        print(f"Saved contribution graph for {current_year} to {contrib_path}")
    else:
        print(f"Failed to save contribution graph for {current_year}")

    # Find achievements section
    achievements_section = driver.find_element(
        By.XPATH, 
        "//div[contains(@class, 'js-profile-editable-replace')]//div[contains(@class, 'border-top color-border-muted pt-3 mt-3 d-none d-md-block')]"
    )
    # Save achievements screenshot
    achievements_path = os.path.join(ASSETS_DIR, "achievements_screenshot.png")
    if achievements_section.screenshot(achievements_path):
        print(f"Saved achievements screenshot to {achievements_path}")
    else:
        print(f"Failed to save achievements screenshot")

except Exception as e:
    print(f"Error capturing data: {e}")

finally:
    driver.quit()