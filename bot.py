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
            
    def wait_for_element(self, selector, by=By.CSS_SELECTOR, timeout=10):
        """Wait for an element to appear on the page"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, selector))
            )
            return element
        except TimeoutException:
            print(f"Element not found after {timeout} seconds: {selector}")
            return None
    
    def close(self):
        """Close the browser"""
        self.driver.quit()

# Example usage:
if __name__ == "__main__":
    bot = WebNavigator()
    
    # Navigate to a website
    bot.navigate_to("http://localhost:8080")
    time.sleep(1)
    
    # Input text into the chat
    bot.input_text("#user-input", "Hello!")
    time.sleep(1)
    
    # Click the send button
    bot.click_element("button")

    # Wait for and get the response
    response = bot.get_text(".bot-message")
    print(f"Bot response: {response}")

    # Input text into the chat
    bot.input_text("#user-input", "I'm doing well, thank you!")
    
    # Click the send button
    bot.click_element("button")

    time.sleep(5)    
    bot.close()
