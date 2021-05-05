focus_selic = [
    5.0, 5.50, 6.13, 6.50, 6.50
]
focus_ipca = [
    4.81,  5.04, 3.61, 3.25, 3.25
]

focus_selic[0] = focus_selic[0]**(126/252)
selic_rates = [x/100 + 0.3477/100 for x in focus_selic]
import sys
sys.path.append(f'../../FinanceHub')

from calendars import DayCounts
import pandas as pd

dc = DayCounts('BUS/252', calendar='anbima')
today = pd.to_datetime('2021-04-26')
d = dc.days(today, pd.to_datetime('2024-12-31'))

a = (1+8.38/100)**(d/252)
print(a)
print(1000*a)