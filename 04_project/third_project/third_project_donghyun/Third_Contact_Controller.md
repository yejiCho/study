```python

from Third_Contact_Model import Model
from Third_Contact_DomainObject import DTO
from Third_Contact_View import View
import Third_Contact_Excepts as Ex


# 도움 주신 분 Do_yeon, Jin_cheon

class Controller:

    def __init__(self):
        self.view = View()
        self.model = Model()

    def inputman(self):
        d = DTO()
        while 1:
            d.name = self.view.name()
            try:
                Ex.name_catch(d.name)
                break
            except Ex.NameError as n:
                self.view.error_man(n)

        while 1:
            d.phno = self.view.phno()
            try:
                Ex.pn_catch(d.phno)
                break
            except Ex.PhoneNumberError as p:
                self.view.error_man(p)
        while 1:
            d.email = self.view.email()
            try:
                Ex.em_catch(d.email)
                break
            except Ex.EmailError as e:
                self.view.error_man(e)
        while 1:
            d.group = self.view.group()
            try:
                Ex.dv_catch(d.group)
                break
            except Ex.DivisionError as d:
                self.view.error_man(d)

        self.model.insert_man(d)

    def showman(self):
        list = self.model.select_man()
        self.view.show_man(list)

    def delman(self):
        while 1:
            name = self.view.name()
            try:
                Ex.name_catch(name)
                break
            except Ex.NameError as n:
                self.view.error_man(n)
        list = self.model.search_man(name)
        self.view.show_man(list)
        index = int(self.view.receive_man())

        dto = list[index-1]
        self.model.delete_man(dto)

    def update_man(self):
        while 1:
            name = self.view.name()
            try:
                Ex.name_catch(name)
                break
            except Ex.NameError as n:
                self.view.error_man(n)
        list = self.model.search_man(name)
        self.view.show_man(list)
        index = int(self.view.receive_man())

        dto = list[index-1]
        while 1:
            dto.name = self.view.name()
            try:
                Ex.name_catch(dto.name)
                break
            except Ex.NameError as n:
                self.view.error_man(n)
        while 1:
            dto.phno = self.view.phno()
            try:
                Ex.pn_catch(dto.phno)
                break
            except Ex.PhoneNumberError as p:
                self.view.error_man(p)
        while 1:
            dto.email = self.view.email()
            try:
                Ex.em_catch(dto.email)
                break
            except Ex.EmailError as e:
                self.view.error_man(e)
        while 1:
            dto.group = self.view.group()
            try:
                Ex.dv_catch(dto.group)
                break
            except Ex.DivisionError as d:
                self.view.error_man(d)

        self.model.up_man(dto)

    # 도움 주신 분 Do_yeon
    def menuman(self):
        doyeon = True
        while doyeon:
            a = self.view.yeji_menu()
            if  a == '1':
                self.inputman()
            elif a == '2':
                self.showman()
            elif a == '3':
                self.update_man()
            elif a == '4':
                self.delman()
            elif a == '5':
                self.view.end_man()
                doyeon = False
            else:
                print("1~5에서 좀 고르세요")
```
