import pymysql as pymysql
from IG_bib import Abre_Conexao, Fecha_Conexao

def fetch_Index_data() -> [str, object]:

    retStatus = "1"

    sql = ""
    sql = sql + " SELECT"
    sql = sql + "     I.IDImage,"
    sql = sql + "     I.Titulo,"
    sql = sql + "     I.Descricao,"
    sql = sql + "     I.IDUserUpload,"
    sql = sql + "     I.Arquivo_Thumb,"
    sql = sql + "     I.Width_Thumb,"
    sql = sql + "     I.Height_Thumb,"
    sql = sql + "     I.Arquivo_Original,"
    sql = sql + "     I.Width_Original,"
    sql = sql + "     I.Height_Original,"  
    sql = sql + "     U.Nome"
    sql = sql + " FROM"
    sql = sql + "     tb_IG_Images I"
    sql = sql + "     LEFT JOIN tb_IG_Users U ON I.IDUserUpload = U.IDUser"
    sql = sql + " ORDER BY "
    sql = sql + "     I.IDImage,"
    sql = sql + "     I.DataCad ASC,"
    sql = sql + "     I.Titulo,"
    sql = sql + "     U.Nome"

    connStatus, objConexao = Abre_Conexao()

    if connStatus == "1":

        try:
            with objConexao.cursor() as cursor:
                cursor.execute(sql)
                results = cursor.fetchall()
                cursor.close()

        except pymysql.OperationalError as e:
            retStatus = "Erro ao conectar executar a query | fetch_Index_data() | " + e.args[0] + " | " + e.args[1]            
            results = None
            
     
        Fecha_Conexao(objConexao) 

    else:
        retStatus = connStatus
        results = None
        

    return [retStatus, results]


    
def insert_image(Titulo: str, 
                 Descricao: str, 
                 IDUserUpload: str,
                 Formato: str,
                 Arquivo_Thumb: str,
                 Width_Thumb: str,
                 Height_Thumb: str,
                 Arquivo_Original: str,
                 Width_Original: str,
                 Height_Original: str) -> str:

    sql = ""
    sql = sql + " INSERT INTO tb_IG_Images"
    sql = sql + " (Titulo, Descricao, IDUserUpload, Width_Original, Height_Original, Formato, Arquivo_Original, Arquivo_Thumb, Width_Thumb, Height_Thumb)"
    sql = sql + " VALUES"
    sql = sql + " ("
    sql = sql + "     '" + Titulo + "',"
    sql = sql + "     '" + Descricao + "',"
    sql = sql + "     " + IDUserUpload + ","
    sql = sql + "     " + Width_Original + ","
    sql = sql + "     " + Height_Original + ","
    sql = sql + "     '" + Formato + "',"
    sql = sql + "     '" + Arquivo_Original + "',"
    sql = sql + "     '" + Arquivo_Thumb + "', "
    sql = sql + "     " + Width_Thumb + ","
    sql = sql + "     " + Height_Thumb
    sql = sql + " )"

    retStatus = "1"

    connStatus, objConexao = Abre_Conexao()

    if connStatus == "1":

        try:
            with objConexao.cursor() as cursor:
                cursor.execute(sql)
                objConexao.commit()
                cursor.close()

        except pymysql.OperationalError as e:
            retStatus = "Erro ao conectar executar a query | insert_image() | " + e.args[0] + " | " + e.args[1]            

        Fecha_Conexao(objConexao) 

    else:
        retStatus = connStatus
        

    return retStatus

