class Login:
    def __init__(self, bot):
        self.bot = bot
        self.homepage = "https://login.aliexpress.com"

    def load_page(self):
        self.bot.move(self.homepage)

    def login(self, email:str, password:str):
        self.load_page()
        email_eid = "fm-login-id"
        password_eid = "fm-login-password"
        login_btn_xpath = "//button[@type='submit']"

        email_box = self.bot.get_element_by_id(email_eid)
        password_box = self.bot.get_element_by_id(password_eid)

        self.bot.send_human_keys(email_box, email)
        self.bot.send_human_keys(password_box, password)
        self.bot.get_element(login_btn_xpath).click()



    