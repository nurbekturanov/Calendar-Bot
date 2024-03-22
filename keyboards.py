import datetime
from typing import Optional

from dateutil.relativedelta import relativedelta
from telegram import InlineKeyboardButton


def month_array(date: datetime.date):
    arr = []
    month_start_date = date - relativedelta(days=date.day - 1)
    next_month_start_date = month_start_date + relativedelta(months=1)
    month_end_date = next_month_start_date - relativedelta(days=1)
    days_in_month = month_end_date.day

    before_offset = month_start_date.weekday()
    after_offset = 6 - month_end_date.weekday()

    for i in range(before_offset + days_in_month + after_offset):
        if i % 7 == 0:
            arr.append([])

        index = i - before_offset
        arr[-1].append((month_start_date + relativedelta(days=index)))
    return arr


def generate_month_keyboard(date: Optional[datetime.date]):
    if date is None:
        date = datetime.date.today()
    prev_month_date = date - relativedelta(months=1)
    next_month_date = date + relativedelta(months=1)

    data = month_array(date)

    keyboard = [
        [
            InlineKeyboardButton(
                "<",
                callback_data=f"date|{prev_month_date.month}|{prev_month_date.year}",
            ),
            InlineKeyboardButton(
                f"{date.strftime('%B')} {date.year}", callback_data=f"year|{date.year}"
            ),
            InlineKeyboardButton(
                ">",
                callback_data=f"date|{next_month_date.month}|{next_month_date.year}",
            ),
        ],
        [
            InlineKeyboardButton(day, callback_data="?")
            for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        ],
    ]

    for row in data:
        temp = []
        for cell_date in row:
            cell_date: datetime.date = cell_date
            temp.append(
                InlineKeyboardButton(cell_date.strftime("%d"), callback_data=f"?")
            )
        keyboard.append(temp)

    return keyboard


def generate_year_keyboard(year: int):
    date = datetime.date(year, 1, 1)
    next_year_date = date + relativedelta(years=1)
    prev_year_date = date - relativedelta(years=1)

    keyboard = [
        [
            InlineKeyboardButton(item[0], callback_data=item[1])
            for item in [
                ["<", f"year|{prev_year_date.year}"],
                [f"{date.year}", f"?"],
                [">", f"year|{next_year_date.year}"],
            ]
        ],
    ]

    for i in range(3):
        temp = []
        for j in range(4):
            month = i * 4 + j + 1
            date = datetime.date(year, month, 1)
            temp.append(
                InlineKeyboardButton(
                    date.strftime("%b"), callback_data=f"date|{date.month}|{date.year}"
                )
            )
        keyboard.append(temp)

    return keyboard
