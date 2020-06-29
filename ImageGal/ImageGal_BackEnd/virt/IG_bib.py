

import pymysql as pymysql

# <pymysql.connections.Connection object at 0x000002B7A36CF550>
def Abre_Conexao() -> pymysql.connections.Connection :

    # Connect to the database
    connection = pymysql.connect(host='imagegallerydb-instance-1.ceyatgym5rai.us-east-1.rds.amazonaws.com',
                                user='ig_user',
                                password='nq!@ub%ncv1Scbcq22DX0a',
                                db='imagegallerydb',
                                cursorclass=pymysql.cursors.DictCursor)

    print("Abre_Conexao: Conexao aberta")

    return connection
                        



def Fecha_Conexao(connection: pymysql.connections.Connection) -> None:
    
    connection.close()

    print("Fecha_Conexao: Conexao fechada")