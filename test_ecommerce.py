import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_ecommerce_login_and_add_to_cart():
    # Initialize the WebDriver (Using Chrome for this execution)
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # Step 1: Navigate to the Mock E-commerce Platform
        driver.get("https://example.com/login") # Standard placeholder for portfolio
        
        # Step 2: Perform secure login testing
        # Utilizing explicit waits for robust elements loading (Industry Best Practice)
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-btn")
        
        # Simulating data-driven inputs
        username_field.send_keys("test_user_qa")
        password_field.send_keys("SecurePassword123!")
        login_button.click()
        
        # Step 3: Validate successful redirection to Dashboard/Shop
        WebDriverWait(driver, 10).until(
            EC.url_contains("/shop")
        )
        print("Success: Login functionality validated securely.")
        
        # Step 4: Search and add a product to the shopping cart
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys("Laptop")
        search_box.submit()
        
        add_to_cart_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-product-id='101']"))
        )
        add_to_cart_btn.click()
        
        # Step 5: Verify Cart Badge updates (Integration and Functional QA Assert)
        cart_badge = driver.find_element(By.CLASS_NAME, "cart-count")
        assert cart_badge.text == "1", f"Expected 1 item in cart, but got {cart_badge.text}"
        print("Success: Product added to cart and state validation passed successfully.")
        
    except Exception as e:
        print(f"Test Execution Failed due to: {str(e)}")
        raise e
        
    finally:
        # Clean up environment after test completion
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    test_ecommerce_login_and_add_to_cart()
