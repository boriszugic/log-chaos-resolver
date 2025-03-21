import argparse
import re
from datetime import datetime, timedelta

def extract_errors(log_file, output_file, filter_hour=None, last_hours=None, specific_date=None):
    errors = []
    pattern = re.compile(r'^(\d{4}-\d{2}-\d{2} (\d{2}):\d{2}:\d{2}) - ERROR: (.+)')
    now = datetime.now()
    
    with open(log_file, 'r') as f:
        for line in f:
            match = pattern.match(line)
            if match:
                timestamp, hour, message = match.groups()
                log_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                
                if filter_hour is not None and int(hour) != filter_hour:
                    continue
                
                if last_hours is not None and log_time < now - timedelta(hours=last_hours):
                    continue
                
                if specific_date is not None and log_time.date() != specific_date:
                    continue
                
                errors.append((timestamp, line.strip()))
    
    errors.sort(key=lambda x: datetime.strptime(x[0], "%Y-%m-%d %H:%M:%S"))
    
    with open(output_file, 'w') as f:
        for _, log_line in errors:
            f.write(log_line + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract and sort ERROR logs from app.log")
    parser.add_argument('--hour', type=int, help="Filter errors by specific hour (0-23)")
    parser.add_argument('--last-hours', type=int, help="Display errors from the last X hours")
    parser.add_argument('--date', type=str, help="Filter errors by specific date (YYYY-MM-DD)")
    args = parser.parse_args()
    
    specific_date = datetime.strptime(args.date, "%Y-%m-%d").date() if args.date else None
    
    extract_errors("app.log", "errors.txt", args.hour, args.last_hours, specific_date)