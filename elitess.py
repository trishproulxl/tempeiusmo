from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.example.com Click on the "About" link
actions = ActionChains(driver)
actions.move_to_element(driver.find_element_by_link_text("About")).click().perform()

# Double-click on the "Contact" link
actions = ActionChains(driver)
actions.move_to_element(driver.find_element_by_link_text("Contact")).double_click().perform()

# Drag and drop the "Element A" to the "Element B"
actions = ActionChains(driver)
actions.drag_and_drop(driver.find_element_by_id("element_a"), driver.find_element_by_id("element_b")).perform()

# Press and hold the "Shift" key while clicking on the "Save" button
actions = ActionChains(driver)
actions.key_down(Keys.SHIFT).click(driver.find_element_by_id("save_button")).key_up(Keys.SHIFT).perform()
