selectSlip = 'SELECT *  FROM account_statement'

InsertSlip = 'INSERT INTO account_statement(`seq`, `ymd`, `entry`, `usage`, `bankcd`, `amount`, `remark`, `payway`, `recode`)   \
              VALUES (null,       %(ymd)s,    %(entry)s,  \
                      %(usage)s,  %(bankcd)s, %(amount)s, \
                      %(remark)s, %(payway)s, %(recode)s)'