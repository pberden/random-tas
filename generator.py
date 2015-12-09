# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:03:42 2015

@author: paul
"""

import csv as csv
import random as r
import datetime as dt
import time

# Set variables
rowcount = 10
dateRange = []

# Define columns
TAS_SOURCE_ID = "NG2-800"
COMPANY_ID = ["1000", "2000", "3000"]
BUSINESS_AREA_ID = ["7000", "9100", "9900"]
CURRENCY_ID = ["USD", "EUR"]
CUSTOMER_ID = ["0000003892",
               "0000003690",
               "0000003893",
               "0000004252",
               "0000003574",
               "0000004254",
               "0000003700",
               "0000003620",
               "0000004253",
               "0000003891",
               "0000100174",
               "0000300701",
               "0000003512",
               "0000003610"]
CUSTOMER_PAYER_ID = CUSTOMER_ID
FINANCIAL_ACCOUNT_ID = ["0000141000",
                        "0000196000",
                        "0000140000"]
FA_DOCUMENT_DATE = dt.date(2015, 12, 9)
# FA_VALID_TO_DATE = ''
# CONTROLLING_AREA_ID = ''
# COST_CENTER_ID = ''
# CC_VALID_TO_DATE = ''
# POSTING_DATE = ''
# PROJECT_ITEM_ID = ''
# CREDIT_CONTROL_AREA_ID = ''
# TRANSACTION_STATUS_ID = ''
# DEBIT_CREDIT_ID = ''
# FINANCIAL_DOCUMENT_ID = ''
# ACCOUNTING_DOCUMENT_ID = ''
# ACCOUNTING_DOCUMENT_ITEM_ID = ''
# FISCAL_YEAR_NUMBER = ''
# FISCAL_PERIOD_NUMBER = ''
# TIME_DATE = ''
# AMOUNT = ''
# OPEN_AMOUNT = ''
# CLEARED_AMOUNT = ''
# CURRENTLY_OPEN_AMOUNT = ''
# CURRENTLY_CLEARED_AMOUNT = ''
# CURRENTLY_LATE_AMOUNT = ''
# CURRENTLY_OPEN_PAST_DUE_AMOUNT = ''
# TRANSACTION_COUNT = ''
# CURRENTLY_OPEN_DAYS = ''
# CURRENTLY_OPEN_LATE_DAYS = ''
# CURRENTLY_OPEN_UNTIL_DUE_DAY = ''
# DAYS_TO_CLOSURE = ''


def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d', prop)
 

# loop
with open('data.csv', 'wb') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for x in range(0, rowcount):
        datawriter.writerow([TAS_SOURCE_ID,
                             r.choice(COMPANY_ID),
                             r.choice(BUSINESS_AREA_ID),
                             r.choice(CURRENCY_ID),
                             r.choice(CUSTOMER_ID),
                             r.choice(CUSTOMER_PAYER_ID),
                             r.choice(FINANCIAL_ACCOUNT_ID),
                             
                             ]
                            )
