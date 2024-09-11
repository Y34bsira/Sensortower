from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Set up the Selenium WebDriver (replace with the path to your chromedriver)
driver = webdriver.Chrome(executable_path='/Users/ysefr1/Downloads/chrome-mac-arm64/Google Chrome for Testing.app')

# Open the Sensor Tower top charts page
driver.get('https://app.sensortower.com/top-charts?country=US&category=0&date=2024-09-11&device=iphone&os=ios')

# Wait for the content to load (you might need to adjust the timeout or use specific conditions)
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'Table__Row'))
)

# Extract data using Selenium
app_names = []
revenues = []
downloads = []
rankings = []
subscription_models = []

# Find all rows in the top charts table
rows = driver.find_elements(By.CLASS_NAME, 'Table__Row')

for row in rows:
    try:
        # Adjust these selectors based on the actual HTML structure
        name = row.find_element(By.CLASS_NAME, 'AppName__StyledAppName').text
        revenue = row.find_element(By.CLASS_NAME, 'Revenue__StyledRevenue').text
        download_count = row.find_element(By.CLASS_NAME, 'Downloads__StyledDownloads').text
        rank = row.find_element(By.CLASS_NAME, 'Rank__StyledRank').text
        subscription = row.find_element(By.CLASS_NAME, 'Subscription__StyledSubscription').text

        # Append to lists
        app_names.append(name)
        revenues.append(revenue)
        downloads.append(download_count)
        rankings.append(rank)
        subscription_models.append(subscription)
    except Exception as e:
        print(f"Error processing row: {e}")

# Save the data to a CSV file
data = pd.DataFrame({
    'App Name': app_names,
    'Revenue': revenues,
    'Downloads': downloads,
    'Ranking': rankings,
    'Subscription Model': subscription_models
})

data.to_csv('sensortower_apps_data.csv', index=False)
print("Data has been saved to sensortower_apps_data.csv")

# Close the browser
driver.quit()
