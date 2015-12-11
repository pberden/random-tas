# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:03:42 2015

@author: paul
"""

import csv as csv
import random as r
# import datetime as dt
import time
import numpy as np

# Set variables
rowcount = 2
startDate = "2014-01-01"
endDate = "2015-12-31"


# Functions
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
# FA_DOCUMENT_DATE = 'Randomly generated in loop'
FA_VALID_TO_DATE = "9999-12-31"
CONTROLLING_AREA_ID = ''
COST_CENTER_ID = ''
CC_VALID_TO_DATE = ''
# POSTING_DATE = 'Same as FA_DOCUMENT_DATE'
PROJECT_ITEM_ID = ["00000000",
                   "00000624",
                   "00001992",
                   "00002073"]
CREDIT_CONTROL_AREA_ID = ["3000",
                          "",
                          "1000"]
TRANSACTION_STATUS_ID = ["Open",
                         "Cleared"]
DEBIT_CREDIT_ID = ["H", "S"]
FINANCIAL_DOCUMENT_ID = ["RV",
                         "DZ",
                         "DR",
                         "DA",
                         "AB",
                         "ZP",
                         "DG",
                         "SA",
                         "EU",
                         "AA",
                         "ZE",
                         "DE"]
ACCOUNTING_DOCUMENT_ID = 100000000  # Starting number left pad one 0
ACCOUNTING_DOCUMENT_ITEM_ID = ["001",
                               "002",
                               "003",
                               "004",
                               "005",
                               "006",
                               "007",
                               "008",
                               "009",
                               "010",
                               "011",
                               "012",
                               "013",
                               "014",
                               "015",
                               "016",
                               "017",
                               "018",
                               "019",
                               "020"]
# FISCAL_YEAR_NUMBER = 'Derive from posting date'
# FISCAL_PERIOD_NUMBER = 'Derive from posting date'
# TIME_DATE = 'Same as FA_DOCUMENT_DATE'
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


# loop
with open('data.csv', 'wb') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=',',
                            quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
    for x in range(0, rowcount):
        FA_DOCUMENT_DATE = randomDate(startDate, endDate, r.random())
        debit_credit = r.choice(DEBIT_CREDIT_ID)
        amount = round(r.gauss(1000, 250), 2)
        if debit_credit == "H":
            amount = round(amount * -1, 2)
        status = np.random.choice(TRANSACTION_STATUS_ID, 1, p=[0.2, 0.8])[0]
        if status == "Open":
            open_amount = amount
            cur_open_pd_amount = np.random.choice([open_amount, 0], 1, p=[0.2, 0.8])[0]
            cur_open_days = int(r.expovariate(1.5) * 20)
        #  Cleared
        else:
            open_amount = 0
            cur_open_pd_amount = 0
            cur_open_days = 0
            cur_clea_amount = amount
            cur_late_amount = np.random.choice([amount, 0], 1, p=[0.2, 0.8])[0]
        datawriter.writerow([TAS_SOURCE_ID,
                             r.choice(COMPANY_ID),
                             r.choice(BUSINESS_AREA_ID),
                             r.choice(CURRENCY_ID),
                             r.choice(CUSTOMER_ID),
                             r.choice(CUSTOMER_PAYER_ID),
                             r.choice(FINANCIAL_ACCOUNT_ID),
                             FA_DOCUMENT_DATE,
                             FA_VALID_TO_DATE,
                             CONTROLLING_AREA_ID,
                             COST_CENTER_ID,
                             CC_VALID_TO_DATE,
                             FA_DOCUMENT_DATE,  # POSTING_DATE
                             np.random.choice(PROJECT_ITEM_ID, 1, p=[0.8, 0.1, 0.05, 0.05])[0],
                             r.choice(CREDIT_CONTROL_AREA_ID),
                             status,
                             debit_credit,
                             np.random.choice(FINANCIAL_DOCUMENT_ID, 1, p=[0.15, 0.14, 0.13, 0.12, 0.10, 0.09, 0.08, 0.06, 0.05, 0.04, 0.03, 0.01])[0],
                             str(ACCOUNTING_DOCUMENT_ID + x).rjust(10, "0"),
                             np.random.choice(ACCOUNTING_DOCUMENT_ITEM_ID, 1, p=[0.10, 0.09, 0.09, 0.08, 0.08, 0.07, 0.07, 0.06, 0.06, 0.05, 0.05, 0.04, 0.04, 0.03, 0.03, 0.02, 0.02, 0.01, 0.007, 0.003])[0],
                             FA_DOCUMENT_DATE[0:4],
                             FA_DOCUMENT_DATE[5:7],
                             FA_DOCUMENT_DATE,  # POSTING_DATE
                             amount,  # AMOUNT
                             open_amount,  # OPEN_AMOUNT
                             "NULL",  # CLEARED_AMOUNT
                             np.random.choice([open_amount, 0], 1, p=[0.2, 0.8])[0],  # CURRENTLY_OPEN_AMOUNT
                             cur_clea_amount,  # CURRENTLY_CLEARED_AMOUNT
                             cur_late_amount,  # CURRENTLY_LATE_AMOUNT
                             cur_open_pd_amount,  # CURRENTLY_OPEN_PAST_DUE_AMOUNT
                             1,  # TRANSACTION_COUNT
                             cur_open_days,  # CURRENTLY_OPEN_DAYS
                             cur_open_days,  # CURRENTLY_OPEN_LATE_DAYS
                             0,  # CURRENTLY_OPEN_UNTIL_DUE_DAY
                             "NULL"]  # DAYS_TO_CLOSURE
                            )
