from common.database.Connect import Connection
from common.database.sql.SelectQuery import SelectComboBySysdiv


def getComboData(category):
    params = {
        'sysdiv': 'COMBO',
        'category': category
    }
    conn = Connection()
    return conn.select(SelectComboBySysdiv, params)


def getComboData_select(category):
    result = getComboData(category)
    result.insert(0,
        {
            'sysdiv': 'COMBO',
            'category': category,
            'code': '-1',
            'name': '전체'
        }
    )
    return result
