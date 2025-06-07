from datetime import date

def format_date(dt: date) -> str:
    return dt.strftime("%d.%m.%Y")

def calc_progress(last: date, next_: date) -> int:
    total_days = (next_ - last).days
    passed_days = (date.today() - last).days

    if total_days <= 0:
        return 100
    return min(100, max(0, int(passed_days / total_days * 100)))

def is_overdue(target_date: date) -> bool:
    return target_date < date.today()
