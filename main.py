
import schedule
import time

from package.job import news

# Will be scheduled to 20:00
schedule.every().days.at("20:00").do(news)

while 1:  # Make the program always running
    schedule.run_pending()
    time.sleep(1)
