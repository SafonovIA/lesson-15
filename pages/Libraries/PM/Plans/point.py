from atf import *
from controls import *
from atf.ui import *


@panel_name('Панель добавления пункта плана')
@templatename('PM/Plans/point:Dialog')
class Dialog(StackTemplate):
    """Панель добавления пункта плана"""
    text_fild = ControlsInputArea()
    executor = Element(By.CSS_SELECTOR, '.plan-PointImplementers__addBtn', 'Исполнитель')
    save_btn_db = ExtControlsButtonsDoubleButton(By.CSS_SELECTOR, '[data-qa="edo3-ReadOnlyStateTemplate__saveButton"]', 'Сохранить')
    lst = ControlsTreeGridView()

    def fill_executor(self, epmloyee):
        """Заполнение поля Исполнители"""

        self.check_open()

        from pages.Libraries.Staff.selectionNew import Stack

        catalog = Stack(self.driver)
        self.executor.click()
        catalog.select(epmloyee)
        self.lst.row(contains_text=epmloyee).should_be(Displayed)

    def fill_comment(self, comment):
        """Заполнение поля Перечень работ"""

        self.check_open()
        self.text_fild.type_in(comment)
        self.text_fild.should_be(ContainsText(comment))

    def safe_point(self):
        """Сохранить пункт плана"""

        self.check_open()
        self.check_close(self.save_btn_db.click)
        delay(0.5)





