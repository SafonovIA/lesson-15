from atf.api.base_api_ui import BaseApiUI
from api.clients.work_plan_list import WorkPlanList


class PlanApiWrapper(BaseApiUI):
    """ПланРабот.СписокПланов"""

    def __init__(self, client):
        super().__init__(client)
        self.plan_api = WorkPlanList(client)

    def delete_document(self, plan_mask, search):
        """Удаление документа
        :param plan_mask: фильтр
        :param search: фильтр поиска
        """

        assert plan_mask, 'Параметр plan_mask не может быть пустым'
        response = self.plan_api.list(search).result
        for i in response:
            if plan_mask in i['Пункты']:
                self.plan_api.delete_timeoff(i['@Документ'])