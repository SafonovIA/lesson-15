from atf.ui import *
from controls import *


class MainWithSteps(Region):
    """
    AuthControls/authForm:MainWithSteps
    Авторизация
    """
    login = TextField(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"] [inputmode="text"]', 'Логин')
    password = TextField(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__password"] [inputmode="text"]', 'Пароль')

    def auth(self, user_login, user_password):
            """
            Авторизация на онлайн
            :param user_login: Логин
            :param user_password: Пароль
            """

            self.login.type_in(user_login + Keys.ENTER)
            self.login.should_be(ExactText(user_login))
            self.password.type_in(user_password + Keys.ENTER)
            self.password.should_not_be(Displayed, wait_time=True)
            self.check_page_load_wasaby()

