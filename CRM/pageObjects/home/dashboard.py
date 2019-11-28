class Sales:
    
    @classmethod
    def txt_sales(cls,driver):
        return driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/section/header/div/div[1]/h1/div/button/span/span[1]/h1")