import pymysql as pymysql
from IG_bib import Abre_Conexao, Fecha_Conexao

def render_Index() -> object:

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

    objConexao = Abre_Conexao()

    try:
        with objConexao.cursor() as cursor:

            cursor.execute(sql)
            results = cursor.fetchall()

            cursor.close()

    finally:
        pass

    Fecha_Conexao(objConexao)   

    return results