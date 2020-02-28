class DTO:
    def __init__(self
                ,id = 0
                ,name = ''
                ,phone_number = ''
                ,email= ''
                ,classification= ''
                ):
        self._id   = id
        self._name = name
        self._phone_number = phone_number
        self._email = email
        self._classification = classification
    # id의 getter,setter
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id_txt):
        self._id = id_txt
    # 이름의 getter,setter
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name_txt):
        self._name = name_txt
    # 전화번호의 getter,setter
    @property
    def phone_number(self):
        return self._phone_number
    @phone_number.setter
    def phone_number(self,phone_number_txt):
        self._phone_number = phone_number_txt
    # 이메일의 getter,setter
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,email_txt):
        self._email = email_txt
    # group의 getter,setter
    @property
    def classification(self):
        return self._classification
    @classification.setter
    def classification(self,classification_txt):
        self._classification = classification_txt
