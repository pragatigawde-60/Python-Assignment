import psutil

#CPU usage threshold percent
threshold =80

def CPU_monitor():
    print("Monitoring CPU usage....\n")


try:
    while True:
        cpu_usage=psutil.cpu_percent(interval=1)
        if cpu_usage>threshold:
            print( f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

except Exception as e:
        print(f"An error : {e}")

if __name__ == "__main__":
    CPU_monitor()
