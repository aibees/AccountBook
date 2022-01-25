from common.database.Connect import Connection
from common.database.sql.SelectQuery import SelectComboBySysdiv


def getComboData(category):
    params = {
        'sysdiv': 'COMBO',
        'category': category
    }
    conn = Connection()
    return conn.select(SelectComboBySysdiv, params)