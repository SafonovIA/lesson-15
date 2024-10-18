from atf.ui import *
from controls import *


class Plans(Region):
    """Реестр Планы работ"""

    add_button = ExtControlsDropdownAddButton(SabyBy.DATA_QA, 'sabyPage-addButton', 'Добавить')
    plan_list = ControlsTreeGridView(By.CSS_SELECTOR, '.edo3-Browser [data-qa="gridWrapper"]', "Список планов")
    control_panel = ControlsPopup()

    def create_doc(self, regulation='План работ'):
        """
        Создание документа
        :param regulation: Выбор параметра
        """

        from pages.Libraries.PM.Plans.dialog import Dialog

        self.add_button.select(regulation)
        plans_card = Dialog(self.driver)
        plans_card.check_open()
        return plans_card

    def exist_plan(self, comment, exist=True):
        """
        Проверка на наличие/отсутствие плана в реестре
        :param comment: Комментарий
        :param exist: bool
        """

        if exist:
            self.plan_list.row(contains_text=comment).should_be(Displayed)
        else:
            self.plan_list.row(contains_text=comment).should_not_be(Displayed)

    def open_plan(self, comment):
        """
        Открыть план
        :param comment: Комментарий
        """

        self.plan_list.row(contains_text=comment).should_be(Displayed).click()

    def delete_plan(self, comment):
        """
        Открыть план
        :param comment: Комментарий
        """
        self.plan_list.check_load()
        self.plan_list.row(contains_text=comment).open_context_menu()
        self.control_panel.select('Удалить')
        self.popup_confirmation.confirm(message='Удалить документ?')
