from helpers import parse_log_line

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                log_data = parse_log_line(line)
                
                if log_data:
                    logs.append(log_data)
                else:
                    print(f"Warning: Could not parse line: {line.strip()}")

    except FileNotFoundError:
        print(f"Warning: File not found: {file_path}")
    except Exception as e:
        print(f"Something else went wrong while loading the logs: {e}")

    return logs            