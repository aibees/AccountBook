import sys, os

from common.database.Connect import Connection
from common.database.sql.SlipQuery import selectSlip

conn = Connection()
result = conn.select(selectSlip, None)
print(result)
