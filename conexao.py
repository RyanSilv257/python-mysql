# conexão com banco de dados
# pip install mysql-connector-python para estabelecer conexão

import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        dbconfig = {
            'host':'127.0.0.1',
            'user':'senai',
            'password':'1234',
            'database':'senai',
        }

        con = mysql.connector.connect(**dbconfig)
        return con
    except(Exception, Error) as error:
        print('Não conectou! ' +str(error)) 

def read(con):
    #Estabelecer conexão
    cursor = con.cursor()

    query = '''SELECT * FROM estudantes;'''

    try:
            cursor.execute(query)

            print('\n\t\t\t ** SENAI - LISTA DE CHAMADA ** ')
            print('\t -- matricula -- \t\t --------------- Nome --------------')
            for campo in cursor.fetchall():
                 print(f'\t{campo[0]} \t \t\t {campo[1]}')
                 # print(f'\t matricula: {campo[0]} - Nome: {campo[1]}')

    except(Exception, Error) as error:
        print('Conectou mas não funcionou! ' +str(error))
    finally:
        if con is not None:
            cursor.close()
            con.close()
            print('\n\n Conexão fechada \n')

def create(con, estudantes):
    #Estabelecer conexão
    cursor = con.cursor()

    #Código SQL
    query = '''INSERT INTO estudantes(matricula, nome) VALUES(%s, %s);'''

    try:
         cursor.executemany(query, estudantes)
         con.commit()
    except(Exception, Error) as error:
         print('Conectou mas não funcionou! ' +str(error))
    finally:
         if con is not None:
              cursor.close()
              con.close()
              print('\n\n Conexão fechada!\n')


def update(con, estudantes):
    # Estabelecer conexão
    cursor = con.cursor()

    #Código SQL
    query = '''UPDATE estudantes SET nome = %s WHERE matricula = %s;'''

    try:
        cursor.executemany(query, estudantes)
        con.commit()
    except(Exception, Error) as error:
        print('Conectou mas não funcionou!' +str(error))
    finally:
        if con is not None:
            cursor.close()
            con.close()
            print ('\n\n Conexão fechada!\n')

        
def delete(con, estudantes):
    # Estabelecer conexão
    cursor = con.cursor()

    #Código SQL
    query = '''DELETE FROM estudantes WHERE matricula = %s;'''

    try:
        cursor.execute(query, estudantes)
        con.commit()
    except(Exception, Error) as error:
        print('Conectou mas não funcionou!' +str(error))
    finally:
        if con is not None:
            cursor.close()
            con.close()
            print('\n\n Conexão fechada!\n')

# Teste

create(conectar(),[('12345', 'Pedro')])
# create(conectar(), [('23456', 'Maria')])
# create(conectar(), [('34567', 'João')])

# update(conectar(), [('Antônio', '12345')])

#delete(conectar(), [('12345')])

read(conectar())
