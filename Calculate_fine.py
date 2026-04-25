# CALCULATE FINE
from datetime import datetime
def calculate_fine(issue_date, allowed_days):
    today = datetime.now()
    total_days = (today - issue_date).days

    if total_days <= allowed_days:
        return 0

    late_days = total_days - allowed_days
    fine = late_days * 10 

    return fine