SelectComboBySysdiv = 'SELECT A.sysdiv, A.category, A.code, A.name \
                         FROM info_code A \
                        WHERE A.sysdiv   = %(sysdiv)s \
                          AND A.category = %(category)s'