import re
from collections import Counter

def parse_log_line(line: str) -> dict:
    pattern = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>.+)'
    match = re.match(pattern, line)
    
    if match:
        return match.groupdict()
    else:
        return {}
 

def count_logs_by_level(logs: list) -> dict:
    levels = [log["level"] for log in logs]
    return dict(Counter(levels))


def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = list(filter(lambda log: log["level"].lower() == level.lower(), logs))
    return list(map(lambda log: f"{log["date"]} {log["time"]} - {log["message"]}", filtered_logs))