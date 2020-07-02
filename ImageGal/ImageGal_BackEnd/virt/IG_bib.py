
import os
import pymysql as pymysql


# <pymysql.connections.Connection object at 0x000002B7A36CF550>
def Abre_Conexao() -> [str, pymysql.connections.Connection] :

    retStatus = "1"

    try:

        # Connect to the database
        connection = pymysql.connect(host='imagegallerydb-instance-1.ceyatgym5rai.us-east-1.rds.amazonaws.com',
                                    user='ig_user',
                                    password='nq!@ub%ncv1Scbcq22DX0a',
                                    db='imagegallerydb',
                                    cursorclass=pymysql.cursors.DictCursor,
                                    connect_timeout=6)

        # print("Abre_Conexao: Conexao aberta")

    except pymysql.OperationalError as e:

        retStatus = "Erro ao conectar no banco de dados | Abre_Conexao() | " + str(e.args[0]) + " | " + str(e.args[1])
        connection = None

    return [retStatus, connection]


def Fecha_Conexao(connection: pymysql.connections.Connection) -> None:
    
    connection.close()
    # print("Fecha_Conexao: Conexao fechada")



def clean(target: str) -> str:
    """
    Cleans the string removing apostrofe (sql injection) and html/javascript tag. Its NOT a final sollution, but helps.
    """

    outFunc = target
    outFunc = outFunc.replace("'", "´")
    outFunc = outFunc.replace("<script>", "[script]")
    outFunc = outFunc.replace("</script>", "[/script]")        
    outFunc = outFunc.replace("<", "[")
    outFunc = outFunc.replace(">", "]")
    
    return outFunc


def getExtFromFileName(filename: str) -> str:
    return os.path.splitext(filename)[1][1:].strip().lower()