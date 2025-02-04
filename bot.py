from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class WebNavigator:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.message_count = 0
    
    def navigate_to(self, url):
        """Navigate to a given URL"""
        self.driver.get(url)
        
    def click_element(self, selector, by=By.CSS_SELECTOR):
        """Click an element on the page"""
        try:
            element = self.wait.until(
                EC.element_to_be_clickable((by, selector))
            )
            element.click()
            return True
        except TimeoutException:
            print(f"Could not find clickable element: {selector}")
            return False
            
    def input_text(self, selector, text, by=By.CSS_SELECTOR):
        """Input text into a form field"""
        try:
            element = self.wait.until(
                EC.presence_of_element_located((by, selector))
            )
            element.clear()
            element.send_keys(text)
            return True
        except TimeoutException:
            print(f"Could not find input element: {selector}")
            return False
            
    def get_text(self, selector, by=By.CSS_SELECTOR):
        """Get text content from an element"""
        try:
            element = self.wait.until(
                EC.presence_of_element_located((by, selector))
            )
            return element.text
        except TimeoutException:
            print(f"Could not find element: {selector}")
            return None

    def wait_for_new_message(self):
        """Wait for a new message to appear"""
        current_messages = len(self.driver.find_elements(By.CSS_SELECTOR, ".bot-message"))
        try:
            WebDriverWait(self.driver, 100).until(
                lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".bot-message")) > current_messages
            )
            return True
        except TimeoutException:
            print("No new message appeared")
            return False
    
    def close(self):
        """Close the browser"""
        self.driver.quit()

# Example usage:
if __name__ == "__main__":
    bot_1 = WebNavigator()
    bot_2 = WebNavigator()

    # Navigate to a website
    bot_1.navigate_to("http://localhost:8080")
    bot_2.navigate_to("http://localhost:8080")
    
    # Input text into the chat
    bot_1.input_text("#user-input", "Hello!")
    
    # Click the send button
    bot_1.click_element("button")

    # Wait for and get the response
    bot_1.wait_for_new_message()
    response_1 = bot_1.get_text(".bot-message")
    print(f"Bot_1 response: {response_1}")

    # Make the bots chat with each other in a loop
    for i in range(5):  # Have 5 back-and-forth exchanges
        # Bot 2 reads Bot 1's response and replies
        bot_2.input_text("#user-input", f"{response_1}")
        bot_2.click_element("button")
        bot_2.wait_for_new_message()
        response_2 = bot_2.get_text(".bot-message")
        print(f"Bot_2 response: {response_2}")

        # Bot 1 reads Bot 2's response and replies
        bot_1.input_text("#user-input", f"{response_2}")
        bot_1.click_element("button")
        bot_1.wait_for_new_message()
        response_1 = bot_1.get_text(".bot-message")
        print(f"Bot_1 response: {response_1}")

    time.sleep(3)
    bot_2.close()
    bot_1.close()
