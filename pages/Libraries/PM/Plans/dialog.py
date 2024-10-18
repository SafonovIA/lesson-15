from controls import *
from atf.ui import *
from atf import *


@panel_name('Панель создания плана')
@templatename('PM/Plans/dialog:Dialog')
class Dialog(StackTemplate):
    """Панель создания плана"""

    executor = Element(By.CSS_SELECTOR, '[data-qa="edo3-Sticker__mainInfo"]', 'Исполнитель')
    executor_plan_object = Element(By.CSS_SELECTOR, '.plan-PointList__object', 'Исполнитель')
    point_plan = ControlsMenuControl(By.CSS_SELECTOR, '[title="Пункт плана"]', 'Пункт плана')
    in_work = ControlsButton(By.CSS_SELECTOR, '[data-qa="edo3-PassageButton__button"]', "На выполнение")
    items_list = ControlsTreeGridView(By.CSS_SELECTOR, '.tw-grid', "Список задач")

    def fill_document(self, **kwargs):
        """Заполнение плана"""

        self.check_open()

        if 'Сотрудник' in kwargs.keys():
            from pages.Libraries.Addressee.popup import Stack
            catalog = Stack(self.driver)
            self.executor.click()
            catalog.select(kwargs['Сотрудник'])
            self.executor.should_be(ContainsText(kwargs['Сотрудник']))
        if 'Комментарий' in kwargs.keys():
            from pages.Libraries.PM.Plans.point import Dialog
            self.point_plan.click()
            point_cart = Dialog(self.driver)
            point_cart.fill_executor(kwargs['Сотрудник'])
            point_cart.fill_comment(kwargs['Комментарий'])
            point_cart.safe_point()
            self.items_list.row(contains_text=kwargs['Комментарий']).should_be(Displayed)

    def run_task(self):
        """Запуск плана в работу"""
        self.in_work.click()
        self.check_close(self.close_btn.click)

    def check_plan(self, **kwargs):
        """Проверка Плана"""

        self.check_open()
        if 'Сотрудник' in kwargs.keys():
            self.executor.should_be(ContainsText(kwargs['Сотрудник']))
        if 'Комментарий' in kwargs.keys():
            self.items_list.row(contains_text=kwargs['Комментарий'])
        if 'Объекты планирования' in kwargs.keys():
            self.executor_plan_object.should_be(ContainsText(kwargs['Объекты планирования']))
        self.check_close(self.close_btn.click)



