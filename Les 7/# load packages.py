# load packages
from pyspark.sql.functions import *
from datetime import datetime, timedelta

# COMMAND ----------

# define boundaries
startdate = datetime.strptime('2023-01-01','%Y-%m-%d')
enddate   = (datetime.now() + timedelta(days=365 * 3)).replace(month=12, day=31)  # datetime.strptime('2023-10-01','%Y-%m-%d')

# COMMAND ----------

# define column names and its transformation rules on the Date column
column_rule_df = spark.createDataFrame([
    ("DateID",              "cast(date_format(date, 'yyyyMMdd') as int)"),     # 20230101
    ("Year",                "year(date)"),                                     # 2023
    ("Quarter",             "quarter(date)"),                                  # 1
    ("Month",               "month(date)"),                                    # 1
    ("Day",                 "day(date)"),                                      # 1
    ("Week",                "weekofyear(date)"),                               # 1
    ("MonthNumberString",   "date_format(date, 'MM')"),                        # 01
    ("DayNumberString",     "date_format(date, 'dd')"),                        # 01
    ("WeekNumberString",    "lpad(weekofyear(date), 2, '0')"),                 # 01
    ("DayOfWeek",           "dayofweek(date)")                                 # 1
  ])