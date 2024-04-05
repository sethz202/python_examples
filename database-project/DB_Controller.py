import mysql.connector
from mysql.connector import Error
import datetime

class DB_Controller:

    def __init__(self):
        self.conn = self.connect_to_database()
        self.cursor = self.conn.cursor()

    def connect_to_database(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='password',
                database='CISC450_PHASE_4'
            )
            return conn
        except Error as e:
            print(f"Error connecting to the database: {e}")
            raise

    def get_users(self):
        query = "SELECT * FROM CISC450_PHASE_4.User;"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Error as e:
            print(f"Error executing query: {e}")
            raise

    def remove_user(self, user_id):
        query = f"DELETE FROM CISC450_PHASE_4.User WHERE UserID = {user_id};"
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print('User successfully removed.')
        except Error as e:
            print(f"Error executing query: {e}")
            raise

    def add_user(self, f_name, l_name, email, extra_info):
        try:
            query = f"INSERT INTO CISC450_PHASE_4.User (FirstName, LastName, Email)  VALUES ('{f_name}', '{l_name}', '{email}');"
            self.cursor.execute(query)
            self.conn.commit()
            recent_id = self.cursor.lastrowid
            if len(extra_info) != 0:
                if len(extra_info) == 3:
                    query = f"INSERT INTO CISC450_PHASE_4.Researcher (UserID, Salary, workHour, JobDescription) VALUES ({recent_id}, {extra_info[0]}, {extra_info[1]}, '{extra_info[2]}');"
                elif len(extra_info) == 2:
                    query = f"INSERT INTO CISC450_PHASE_4.Customer_Support (UserID, DeptName, PhoneNumber) VALUES ({recent_id}, '{extra_info[0]}', '{extra_info[1]}');"
                self.cursor.execute(query)
                self.conn.commit()
            print('User successfully added.')
        except Error as e:
            print(f"Error executing query: {e}")
            raise

    def get_mstructure(self, type):
        query = f"SELECT * FROM CISC450_PHASE_4.{type}structure;"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Error as e:
            print(f"Error executing query: {e}")
            raise

    def add_issue(self, information):
        try:
            if information[1] == None:
                information[1] = 1
            date = datetime.datetime.now()
            date_formated = date.strftime("%Y-%m-%d")
            query = f"INSERT INTO CISC450_PHASE_4.Customer_Support_Case (UserID, SupportID, Issue, DateReported, ErrorType)  VALUES ({information[0]}, {information[1]}, '{information[2]}', '{date_formated}', '{information[3]}');"
            self.cursor.execute(query)
            self.conn.commit()
            print('Issue successfully added.')
        except Error as e:
            print(f"Error executing query: {e}")
            raise

    def get_open_support_cases(self):
        query = "SELECT * FROM CISC450_PHASE_4.Customer_Support_Case;"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Error as e:
            print(f"Error executing query: {e}")
            raise

    def add_information_meso(self,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15):
        add_query = '''INSERT INTO Mesostructure
                        (StromatoliticID,ThromboliticID,ImageID,SampleIDKey,FieldDescription,RockDescription,GeneralType,
                        LaminaProperties,LaminaThickness,TextureOne,Amplitude,TextureTwo,Grains,SynopticRelief,Wavelength)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        data_to_insert = (q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15)
        self.add_image(q3)
        try:
            self.cursor.execute(add_query, data_to_insert)
            self.conn.commit()
            print('Successfully added to Meso-structure microbialites!')
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def add_information_macro(self,q1,q2,q3,q4,q5,q6,q7):
        add_query = '''INSERT INTO Macrostructure
                        (WaypointID,MesostructureID,MegaStructureID,ImageID,MacroinfoID,SectionHeight,Comments)
                        VALUES (%s,%s,%s,%s,%s,%s,%s)'''
        data_to_insert = (q1,q2,q3,q4,q5,q6,q7)
        
        try:
            self.cursor.execute(add_query, data_to_insert)
            self.conn.commit()
            print('Successfully added to Macro-structure microbialites!')
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def remove_information_meso(self, id):
        remove_query = "DELETE FROM Mesostructure WHERE MesostructureID = %s;"

        try:
            self.cursor.execute(remove_query, (id,))
            self.conn.commit()
            print('Successfully removed from Meso-structure microbialites!')
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def remove_information_macro(self, id):
        remove_query = "DELETE FROM Macrostructure WHERE MacrostructureID = %s;"

        try:
            self.cursor.execute(remove_query, (id,))
            self.conn.commit()
            print('Successfully removed from Macro-structure microbialites!')
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def add_image(self, id):
        add_query = f"INSERT INTO Mesostructure_Image (ImageID, Image) VALUES ({id}, null);"
        try:
            self.cursor.execute(add_query)
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")