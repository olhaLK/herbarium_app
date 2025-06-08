from datetime import date

def format_date(d: date) -> str:
    return d.strftime("%d.%m.%Y")

def calc_progress_adaptive(last_date: date, interval_days: int, max_days: int) -> int:
    today = date.today()
    days_passed = (today - last_date).days

    if days_passed >= max_days:
        return 0

    if days_passed <= interval_days:
        return 100

    overflow = days_passed - interval_days
    progress = max(0, 100 - int((overflow / (max_days - interval_days)) * 100))
    return progress

