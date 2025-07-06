import os
from datetime import datetime

def capture_screenshot(driver, test_method_name, test_file_name):
    # Use the passed-in test file name
    folder_name = os.path.splitext(test_file_name)[0]

    # Go to project root (Automation_framework)
    base_dir = os.path.dirname(os.path.dirname(__file__))

    # Create Screenshots/test_login/
    screenshot_dir = os.path.join(base_dir, "Screenshots", folder_name)
    os.makedirs(screenshot_dir, exist_ok=True)

    # Create file: Test_Login_Title_fail_timestamp.png
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{test_method_name}_fail_{timestamp}.png"
    file_path = os.path.join(screenshot_dir, file_name)

    driver.save_screenshot(file_path)
    print(f"📸 Screenshot saved to: {file_path}")
