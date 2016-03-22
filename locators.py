from selenium.webdriver.common.by import By


class MainPageLocators(object):
    HEADER          = (By.XPATH, "html/body/div[3]/div[1]/nav[1]/div/div/a")
    SIGNINMENU      = (By.LINK_TEXT, "Sign In")
    SITELANGUAGE    = (By.XPATH, "html/body/div[3]/div[1]/nav[1]/div/span/div/div/a/span")
    LANGUAGEMENU    = (By.XPATH, "html/body/div[3]/div[1]/nav[1]/div/span/div/ul")
    EMAILINPUT      = (By.ID, "username_id")
    PASSWORDINPUT   = (By.ID, "password_id")
    SIGNINBUTTON    = (By.XPATH, "html/body/div[3]/div/div[2]/div/form/div[6]/button")


class DashboardPageLocators(object):
    HEADER          = (By.XPATH, ".//*[@id='top']/nav[1]/div/div/a")
    MENUTOP         = (By.ID, "bs-example-navbar-collapse-1")
