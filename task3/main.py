import sys
from file_reader import load_logs
from helpers import count_logs_by_level, filter_logs_by_level
from displayers import display_log_counts, display_log_details
from pathlib import Path

if __name__ == "__main__":
    try:
        path = Path(sys.argv[1])    

        if not path.exists() or not path.is_file():
            raise ValueError("Warning: Provided path is not a valid file.")

        parsed_logs = load_logs(path)
        log_stats = count_logs_by_level(parsed_logs)
        display_log_counts(log_stats)

        if len(sys.argv) > 2: 
            filtered_logs = filter_logs_by_level(parsed_logs, sys.argv[2])
            display_log_details(filtered_logs, sys.argv[2])

    except IndexError:
        print(f"Warning: Missing path argument")
    except ValueError as e:
        print(f"Warning: {e}")
    except Exception as e:
        print(f"Something else went wrong: {e}")