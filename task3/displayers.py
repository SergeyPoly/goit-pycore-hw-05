def display_log_counts(counts: dict) -> None:
    print(f"{'Рівень логування':<16} | {'Кількість':<8}")
    print("-" * 17 + "|" + "-" * 10)

    for level, count in counts.items():
        print(f"{level:<16} | {count:<8}")


def display_log_details(logs: list, level: str) -> None:
    if logs:
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in logs:
            print(log)
    else:
        print(f"\nNo logs found for level '{level.upper()}'")