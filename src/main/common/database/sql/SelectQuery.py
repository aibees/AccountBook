SelectComboBySysdiv = 'SELECT A.sysdiv, A.category, A.code, A.name \
                         FROM info_code A \
                        WHERE A.sysdiv   = %(sysdiv)s \
                          AND A.category = %(category)s'

CreditCardTransition = 'select substr(a.ymd, 1, 6) as ym                                                             \
                             , (select b.mnit1 from info_code b where b.category = "PAYWAY" and b.code = a.payway) as name \
                             , sum(a.amount) as provamt                                                              \
                          from account_statement a                                                                   \
                         where entry = "1"                                                                           \
                           and a.payway in ("00", "01", "02")                                                        \
                           and a.usage not in ("00", "01", "09") /* 전월이월, 계좌이체, 이행 */                          \
                         group by substr(a.ymd, 1, 6), payway                                                        \
                         order by  substr(a.ymd, 1, 6)'