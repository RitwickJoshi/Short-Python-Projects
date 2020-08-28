import sqlite3
from sqlite3 import Error
import os
import admin
    
def create_user_database(db_path):
    connection_user_database_cursor = sqlite3.connect(db_path).cursor()
    query = '''CREATE TABLE USER_TABLE
        (
            USERNAME TEXT PRIMARY KEY NOT NULL,
            PSSWORD TEXT NOT NULL
        );'''
    try:
        connection_user_database_cursor.execute(query)
    except Error as e:
        print(e)



if __name__ == "__main__":
    admin_password = '123'
    create_user_database(fr'{os.getcwd()}\db\users_database.db')
    print(fr'{os.getcwd()}\db\users_database.db')
    user_or_admin = 0
    auth_user = sqlite3.connect(os.getcwd()+r"\db\users_database.db")
    auth_cursor = auth_user.cursor()
    while user_or_admin != 4:
        user_or_admin = int(input('1.User Login\n2.Admin Login\n3.New User \n4.Exit \nEnter choice: '))
        print(user_or_admin)
        if user_or_admin == 1:
            # asking for username and password
            input_username = input('Enter the username: ')
            input_password = input('Enter the password: ')
            input_password = str(input_password)
            #getting password from user database
            query = 'SELECT PSSWORD FROM USER_TABLE WHERE USERNAME=?'
            auth_cursor.execute(query,(input_username, ))
            db_passwd = auth_cursor.fetchall()
            print(db_passwd)
            for psswd in db_passwd:
                if psswd == input_password:
                    connection_user = sqlite3.connect(os.getcwd()+rf"\db\{input_username}.db")
                    print('*'*15)
                    print('Commands: ')
                    print('q = quit Program: ')
                    print('r = retrieve file: ')
                    print('s = store file: ')
                    print('*'*15)
                    input_ = input('choice:')
                    if input_ == 'q':
                        break
                    elif input_ == 'r':
                        print(connection_user.execute('SELECT * FROM SAFE'))
                        file_name = input('Enter the name of the file: ')
                        file_type = input('Enter the extenstion of the file: ')
                        FILE_ = file_name+'.'+file_type
                else:
                    print(f'{psswd} in else')

        elif user_or_admin == 3:
            input_username = input('Enter the username: ')
            auth_user = sqlite3.connect(os.getcwd()+rf"\db\users_database.db")
            try:
                auth_cursor.execute(" SELECT USERNAME FROM USER_TABLE ")
                users_list = auth_cursor.fetchall()
                print(users_list)
            except Error as e:
                users_list = ['']
            print(len(users_list))
            if len(users_list) == 0:
                input_password = input('Enter the password: ')
                query = f'INSERT INTO USER_TABLE(USERNAME, PSSWORD) VALUES (?,?)'
                into_table = (input_username,input_password)
                auth_cursor.execute(query,into_table)
                connection_user = sqlite3.connect(os.getcwd()+rf"\db\{input_username}.db")
                try:
                    connection_user.execute(
                        ''' 
                        CREATE TABLE SAFE
                        (FILE_NAME TEXT NOT NULL,
                        EXTENSION TEXT NOT NULL,
                        FILES BLOB NOT NULL);
                        '''
                    )
                    print("Your Safe has been created")
                except:
                    print('some error while creating safe maybe safe already exist')

            for name in users_list:
                if input_username in name:
                    print('username exits')
                    break
                else :
                    input_password = input('Enter the password: ')
                    query = f'INSERT INTO USER_TABLE(USERNAME, PSSWORD) VALUES (?,?)'
                    into_table = (input_username,input_password)
                    auth_cursor.execute(query,into_table)
                    connection_user = sqlite3.connect(os.getcwd()+rf"\db\{input_username}.db")
                    try:
                        connection_user.execute(
                            ''' 
                            CREATE TABLE SAFE
                            (FILE_NAME TEXT NOT NULL,
                            EXTENSION TEXT NOT NULL,
                            FILES BLOB NOT NULL);
                            '''
                        )
                        print("Your Safe has been created")
                    except:
                        print('some error while creating safe maybe safe already exist')
                    break
                
                
        