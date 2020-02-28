from DTO import DTO
import cx_Oracle


class ContactDB:
    def __init__(self):
        self.con_name = 'ora_user/1234@localhost:1521/xe'

    def all_info(self,sql):
        conn = cx_Oracle.connect(self.con_name)
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    
    def one_info(self,sql):
        conn = cx_Oracle.connect(self.con_name)
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data

    def commit_info(self,sql,data):
        conn = cx_Oracle.connect(self.con_name)
        cursor = conn.cursor()
        cursor.execute(sql, data)
        cursor.close()
        conn.commit()
        conn.close()

# (id, name, phno, email, grpno)
# (data,)
    def commit(self,sql):
        conn = cx_Oracle.connect(self.con_name)
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()


    def insert_db(self,dto: DTO()):
        check_sql =  "select max(pri_num) from contact"
        num = self.one_info(check_sql)
        id = num[0]+1 if num[0] else 1
        cls_sql = f"""SELECT cls_num
                      FROM   classification
                      WHERE   cls_name = '{dto.classification}'
                    """
        cls = self.one_info(cls_sql)
        clsid = 0
        if cls:
            clsid = cls[0]        
        else:
            sql = "SELECT MAX(CLS_NUM) FROM classification"
            num = self.one_info(sql)
            clsid = num[0]+1 if num[0] else 1

            sql = "INSERT INTO classification VALUES(:1,:2)"
            data = (clsid, dto.classification)
            self.commit_info(sql, data)
        
        
        contact_sql = "INSERT INTO contact VALUES(:1,:2,:3,:4,:5)"
        data = (id, dto.name, dto.phone_number, dto.email, clsid)
        self.commit_info(contact_sql, data)


    def select_db(self):
        sql = """
            SELECT contact.pri_num,contact.pri_name,contact.phone_num,contact.email,classification.cls_name
            FROM   classification, contact
            WHERE  classification.cls_num = contact.cls_num
            """
        all_info = self.all_info(sql)
        
        dto_list = [DTO(row[0], row[1], row[2], row[3], row[4]) 
                    for row in all_info]  
        return dto_list


    def delete_db(self,dto):
        input_name = dto
        sql =f"""
            SELECT contact.pri_num,contact.pri_name,contact.phone_num,contact.email,classification.cls_name
            FROM   classification, contact
            WHERE  classification.cls_num = contact.cls_num
            AND    contact.pri_name = '{input_name}'
            """
        data = self.all_info(sql)
        del_list = [DTO(row[0], row[1], row[2], row[3], row[4]) 
                    for row in data]
        return del_list
    

    def delete_model(self,dto):
        input_id = dto.id
        sql = f"""
            DELETE FROM CONTACT
            WHERE  PRI_NUM = '{input_id}'
            """
        self.commit(sql)