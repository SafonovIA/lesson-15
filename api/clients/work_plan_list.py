from atf.api.base_api_ui import BaseApiUI
from atf.api.helpers import *


class WorkPlanList(BaseApiUI):
    """ПланРабот.СписокПланов"""
    def list(self, search):
        """Список планов
        :param search:
        :return:
        """

        params = generate_record_list(
            iterative_list=True,
            new_navigation=True,
            translit_search=False,
            МастерФильтр=-1,
            СостояниеПлана=-1,
            СостояниеПунктов=0,
            ФильтрДатаП=(None, 'Строка'),
            ФильтрДатаС=(None, 'Строка'),
            ФильтрПоМаске=search,
            ФильтрПринадлежность=0
        )

        return self.client.call_rrecordset(method='ПланРабот.СписокПланов', **params)

    def delete_timeoff(self, idd):
        """
        Удаление документа
        :param idd:
        """
        self.client.call_rvalue(method='Документ.УдалитьДокументы', ИдО=idd)
