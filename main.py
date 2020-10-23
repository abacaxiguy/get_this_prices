import functions

if functions.validate_today_date():
    functions.save_into_sheet()
    functions.add_day()