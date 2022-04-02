selectSlipByCondition = 'select a.seq, a.ymd, a.remark,                     \
                  case when a.entry = 0 then amount else 0 end as input,    \
                  case when a.entry = 1 then amount else 0 end as output,   \
       (select b.name                                                       \
          from info_code b                                                  \
         where b.sysdiv = "COMBO"                                           \
         and b.category = "USAGE"                                           \
         and b.code = a.usage) as "usage",                                  \
       (select b.name                                                       \
          from info_code b                                                  \
         where b.sysdiv = "COMBO"                                           \
           and b.category = "BANK"                                          \
           and b.code = a.bankcd) as "bank",                                \
       (select b.name                                                       \
          from info_code b                                                  \
         where b.sysdiv = "COMBO"                                           \
           and b.category = "PAYWAY"                                        \
           and b.code = a.payway) as "payway",                              \
       substr(a.recode, 12, 8) as times                                     \
  from account_statement a                                                  \
 where a.ymd between %(frdate)s and %(todate)s                              \
   and a.usage like concat(%(usage)s  , "%%")                               \
   and a.bankcd like concat(%(bankcd)s, "%%")                               \
   and a.payway like concat(%(payway)s, "%%")                               \
   and a.remark like %(search)s                                             \
 order by ymd, times '

InsertSlip = 'INSERT INTO account_statement(`seq`, `ymd`, `entry`, `usage`, `bankcd`, `amount`, `remark`, `payway`, `recode`)   \
              VALUES (null,       %(ymd)s,    %(entry)s,  \
                      %(usage)s,  %(bankcd)s, %(amount)s, \
                      %(remark)s, %(payway)s, %(recode)s)'