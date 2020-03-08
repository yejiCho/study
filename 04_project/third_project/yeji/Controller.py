from View import View
from DB import ContactDB 
from DTO import DTO
import Error

class Controller:
    def __init__(self):
        self.db = ContactDB()
        self.View = View()
        # self.dto = DTO()

    def execute(self):
        while True:
            main_num = self.View.main()
            if main_num == '1':
                self.add()
            elif main_num == '2':
                self.select()
            elif main_num == '3':
                self.update()
            elif main_num == '4':
                self.delete()
            elif main_num == '5':
                print("종료합니다.")
                break
            else:
                print("없는 번호입니다. 다시 입력하세요.")
    
    def add(self):
        dto = self.View.insert_index()
        email = dto.email
        try:
            email = Error.email_error(email)
            self.db.insert_db(dto)
        except Error.regex_exception as error_e:
            return print(error_e)
        
    def select(self):
        dto_list = self.db.select_db()
        self.View.select_index(dto_list)

    def update(self):
        dto = DTO()
        name = self.View.input_name()
        dto.name = name
        del_list = self.db.delete_db(dto.name)
        self.View.delete_index(del_list)
        delete_name = self.View.find_index()
        self.db.delete_model(del_list[delete_name - 1])
        dto = self.View.insert_index()
        self.db.insert_db(dto)

    
    def delete(self):
        dto = DTO()
        name = self.View.input_name()
        dto.name = name
        del_list = self.db.delete_db(dto.name)
        self.View.delete_index(del_list)
        delete_name = self.View.find_index()
        self.db.delete_model(del_list[delete_name - 1])


controller = Controller()
controller.execute()
