import datetime


from database.database_connect import conn

async def query_score_sql(id: int):
    try:
        cursor = conn.cursor()
        score_num = cursor.execute('SELECT sum(currency) FROM nanami.daliy where qqnum={}'.format(id))
        conn.commit()
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        return data_dict[0]["sum(currency)"]
    finally:
        cursor.close()
        



async def shopping_sql(id: int, date: datetime, spend: int):
    try:
        cursor = conn.cursor()
        cursor.execute('insert into daliy(`qqnum`,`date`,`currency`)values({},\'{}\',{})'.format(id, date, spend))
        conn.commit()
    finally:
        cursor.close()