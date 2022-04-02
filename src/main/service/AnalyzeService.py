from common.database.Connect import Connection
from common.database.sql.SelectQuery import CreditCardTransition


def getTransitionByCreditCardData():
    conn = Connection()
    data = conn.select(CreditCardTransition, None)
    ym_set = set()
    data_set = {}

    for d in data:
        if d['ym'] not in ym_set:
            ym_set.add(d['ym'])

        payway = d['name']
        if payway in data_set:
            d_list = data_set[payway]
            d_list.append(d)
            data_set[payway] = d_list
        else:
            data_set[payway] = [d]

    ym_set = list(ym_set)
    plotDict = {}

    for key in data_set.keys():
        data_payway = data_set[key]
        # for ym in ym_set:






    return conn.select(CreditCardTransition, None)