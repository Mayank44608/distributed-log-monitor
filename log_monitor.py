log_file = [
    "INFO Server started",
    "INFO User login successful",
    "ERROR Database connection failed",
    "WARNING Memory usage high",
    "ERROR Payment service timeout"
]

for log in log_file:
    if "ERROR" in log:
        print("Critical issue detected:", log)
    elif "WARNING" in log:
        print("Warning detected:", log)
    else:
        print("Normal log:", log)
