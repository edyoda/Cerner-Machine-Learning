class Auth:
    
    @classmethod
    def tb_email(cls,driver):
        return driver.find_element_by_id("username")
    
    @classmethod
    def tb_password(cls,driver):
        return driver.find_element_by_id("password")
    
    @classmethod
    def btn_password(cls,driver):
        return driver.find_element_by_id("loginBtn")
    
    @classmethod
    def link_contacts(cls,driver):
        element = driver.find_element_by_partial_link_text("Contacts")
        return element

    @classmethod
    def sub_link_contacts(cls,driver):
        element = driver.find_element_by_id("nav-secondary-contacts")
        return element
