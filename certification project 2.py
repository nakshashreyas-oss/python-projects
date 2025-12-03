'''Solution
for Time Calculator'''


def add_time(start, duration, day=None):
    # Weekday list for indexing
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Step 1: Parse start time
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))

    # Convert to 24-hour format
    if period.upper() == 'PM' and start_hour != 12:
        start_hour += 12
    elif period.upper() == 'AM' and start_hour == 12:
        start_hour = 0

    # Step 2: Parse duration
    dur_hour, dur_minute = map(int, duration.split(':'))

    # Step 3: Add time
    total_minutes = start_minute + dur_minute
    extra_hour = total_minutes // 60
    final_minute = total_minutes % 60

    total_hours = start_hour + dur_hour + extra_hour
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    # Step 4: Convert back to 12-hour format
    if final_hour_24 == 0:
        final_hour = 12
        final_period = 'AM'
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        final_period = 'AM'
    elif final_hour_24 == 12:
        final_hour = 12
        final_period = 'PM'
    else:
        final_hour = final_hour_24 - 12
        final_period = 'PM'

    # Step 5: Format result
    new_time = f"{final_hour}:{str(final_minute).zfill(2)} {final_period}"

    # Step 6: Handle optional weekday
    if day:
        day_index = weekdays.index(day.capitalize())
        new_day_index = (day_index + days_later) % 7
        new_day = weekdays[new_day_index]
        new_time += f", {new_day}"

    # Step 7: Add day info
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time