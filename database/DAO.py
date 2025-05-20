from database.DB_connect import DBConnect
from model.Airport import Airport
from model.Flight import Flight


class dao():
    def __init__(self):
        pass

    @staticmethod
    def get_airports():
        areoporti = {}
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
                areoporti[airport["ID"]] = (Airport(**airport))
            cursor.close()
        conn.close()
        return areoporti

    @staticmethod
    def get_flights(u: Airport, v: Airport):
        flights = []
        conn = DBConnect.get_connection()
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor(dictionary=True)
            query = """SELECT *
                        FROM flights
                        WHERE ORIGIN_AIRPORT_ID = %s
                        AND DESTINATION_AIRPORT_ID = %s
                               """
            cursor.execute(query, (u.ID, v.ID))
            res = cursor.fetchall()
            for flight in res:
                flights.append(Flight(**flight))
            cursor.close()

            res = []

            cursor = conn.cursor(dictionary=True)
            query = """     SELECT *
                            FROM flights f
                            where 
                            f.ORIGIN_AIRPORT_ID  = %s
                            and f.DESTINATION_AIRPORT_ID = %s
                            or 
                            f.ORIGIN_AIRPORT_ID  = %s
                            and f.DESTINATION_AIRPORT_ID = %s
                                           
                                           """
            cursor.execute(query, (u.ID, v.ID, v.ID, u.ID))
            res = cursor.fetchall()
            for flight in res:
                flights.append(Flight(**flight))
            cursor.close()

        conn.close()
        return flights

    @staticmethod
    def get_avg_distance(u: Airport, v: Airport):
        conn = DBConnect.get_connection()
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor()
            query = """     SELECT avg(f.distance)
                            FROM flights f
                            where 
                            f.ORIGIN_AIRPORT_ID  = %s
                            and f.DESTINATION_AIRPORT_ID = %s
                            or 
                            f.ORIGIN_AIRPORT_ID  = %s
                            and f.DESTINATION_AIRPORT_ID = %s

                                                       """
            cursor.execute(query, (u.ID, v.ID, v.ID, u.ID))
            avg = cursor.fetchone()
            cursor.close()
            conn.close()
            if avg[0] is None:
                return -1
            else:
                return int((avg[0]))

    @staticmethod
    def get_flights_filtered(u: Airport, v: Airport, media: int):
        flights = []
        conn = DBConnect.get_connection()
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor(dictionary=True)
            query = """select *  
                        from flights f 
                        where (
                            select avg(f.distance)  
                            from flights f 
                            where f.ORIGIN_AIRPORT_ID  = %s
                            and f.DESTINATION_AIRPORT_ID = %s
                            or f.ORIGIN_AIRPORT_ID  = %s
                            and f.DESTINATION_AIRPORT_ID = %s
                            ) > %s"""
            cursor.execute(query, (u.ID, v.ID, v.ID, u.ID, media))
            res = cursor.fetchall()
            for flight in res:
                flights.append(Flight(**flight))
            cursor.close()

            res = []

            cursor = conn.cursor(dictionary=True)
            query = """SELECT *
                                            FROM flights
                                            WHERE ORIGIN_AIRPORT_ID = %s
                                            AND DESTINATION_AIRPORT_ID = %s
                                                   """
            cursor.execute(query, (v.ID, u.ID))
            res = cursor.fetchall()
            for flight in res:
                flights.append(Flight(**flight))
            cursor.close()

        conn.close()
        return flights

    @staticmethod
    def get_edges():
        conn = DBConnect.get_connection()
        if conn is None:
            print("Connection failed")
        else:
            res = []
            cursor = conn.cursor()
            query = """select t1.ORIGIN_AIRPORT_ID, t1.DESTINATION_AIRPORT_ID,
                        coalesce(t1.voli_tot, 0) + coalesce(t2.voli_tot, 0) as voli,
                        coalesce(t1.DISTAZATOT, 0) + coalesce(t2.DISTAZATOT, 0) as tot_distanza
                        from (select f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, count(*) as "voli_tot", sum(f.DISTANCE) as DISTAZATOT
                        from flights f 
                        group by f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID ) t1
                        left join (select f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, count(*) as "voli_tot", sum(f.DISTANCE) as DISTAZATOT
                        from flights f 
                        group by f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID ) t2
                        on t1.ORIGIN_AIRPORT_ID = t2.DESTINATION_AIRPORT_ID and t1.DESTINATION_AIRPORT_ID = t2.ORIGIN_AIRPORT_ID
                        """
            cursor.execute(query)
            for line in cursor:
                res.append(line)
            cursor.close()
            conn.close()
            return res


if __name__ == "__main__":
    for e in dao.get_edges():
        print(e)
