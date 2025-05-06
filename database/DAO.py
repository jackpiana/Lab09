from database.DB_connect import DBConnect
from model.Airport import Airport


class dao():
    def __init__(self):
        pass

    @staticmethod
    def get_airports():
        areoporti = []
        conn = DBConnect.get_connection()
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor(dictionary = True)
            query = """
                    SELECT *
                    FROM airports
                    """
            cursor.execute(query, ())
            res = cursor.fetchall()
            for airport in res:
                areoporti.append(Airport(**airport))
            cursor.close()
        conn.close()
        return areoporti


if __name__ == "__main__":
    areoporti = dao.get_airports()
    for areoporto in areoporti:
        print(areoporto)
