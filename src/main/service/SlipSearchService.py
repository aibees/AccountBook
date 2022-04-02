from common.database.Connect import Connection
from common.database.sql.SlipQuery import selectSlipByCondition


def SearchDataByPeriod(data):
    conn = Connection()
    return conn.select(selectSlipByCondition, data)

