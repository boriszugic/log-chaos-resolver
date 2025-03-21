# Log Chaos Resolver Solution

## Overview

This is my solution to the **Kubenatives DevOps Code Challenge: Log Chaos Resolver** by Sharon Sahadevan: https://github.com/sharonsahadevan/devops-code-quests

## Challenge Details

The task was to:

1. **Extract all lines with "ERROR"** from a log file.
2. **Sort** the error lines by timestamp.
3. **Save** the results in a file called `errors.txt`.
4. **Bonus**: Implement a command-line flag (`--hour`) to filter logs by a specific hour.

I didn't stop there, however:

`--date` flag: Filters logs by a specific date in YYYY-MM-DD format, so you can easily extract errors from a particular day.

`--last-hours` flag: Filters logs to only include errors that occurred within the last X hours from the current time.

## Sample Output

Given the following log data:

```txt
2025-03-15 13:45:12 - INFO: System starting up
2025-03-15 14:30:00 - ERROR: Disk full
2025-03-15 14:32:15 - INFO: User logged in
2025-03-15 15:10:22 - ERROR: Connection timeout
2025-03-15 14:55:47 - DEBUG: Processing request
2025-03-15 13:50:00 - ERROR: Invalid input received
2025-03-15 16:00:01 - INFO: Shutdown initiated
2025-03-15 14:15:30 - ERROR: Memory limit exceeded
```

The extracted `errors.txt` file will contain if no flags are provided:

```txt
2025-03-15 13:50:00 - ERROR: Invalid input received
2025-03-15 14:30:00 - ERROR: Disk full
2025-03-15 14:15:30 - ERROR: Memory limit exceeded
2025-03-15 15:10:22 - ERROR: Connection timeout
```
