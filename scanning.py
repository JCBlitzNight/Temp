import csv
import datetime
from splunklib import client

SPLUNK_HOST = "your_splunk_host"
SPLUNK_PORT = 8089  
SPLUNK_USERNAME = "your_username"
SPLUNK_PASSWORD = "your_password"

searchearliest = "2022-09-22 00:00:00"  
searchlatest = "2022-09-23 00:00:00"

service = client.connect(
   host=SPLUNK_HOST, 
   port=SPLUNK_PORT,
   username=SPLUNK_USERNAME,
   password=SPLUNK_PASSWORD
)

jobs_per_interval = 4
max_result_rows = 50000 

starttime = datetime.datetime.strptime(searchearliest, "%Y-%m-%d %H:%M:%S")
endtime = datetime.datetime.strptime(searchlatest, "%Y-%m-%d %H:%M:%S")

timedelta = (endtime - starttime) / 16

for i in range(16):

    interval_start = starttime + i*timedelta
    interval_end = interval_start + timedelta

    for j in range(jobs_per_interval):

        job_start = interval_start + j*(timedelta/jobs_per_interval) 
        job_end = job_start + (timedelta/jobs_per_interval)

        searchquery_time = "%s %s" % (job_start.strftime("%Y-%m-%d %H:%M:%S"), job_end.strftime("%Y-%m-%d %H:%M:%S"))

        searchquery = "search * | timechart span={} count".format(searchquery_time)

        job = service.jobs.create(searchquery, count=max_result_rows)

        while True:
            job.refresh()  
            if job["isDone"] == "1":
                break

        results = []
        
        offset = 0
        reader = job.results(count=max_result_rows, offset=offset)
        while reader:
            results.extend(list(reader))
            offset += max_result_rows 
            reader = job.results(count=max_result_rows, offset=offset)
            
        # Output results to CSV  
        hr1 = int(interval_start.strftime("%H"))
        hr2 = int(interval_end.strftime("%H"))
            
        filename = "cp_{}_{}.csv".format(str(hr1).zfill(2), str(hr2).zfill(2))
        
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(results)

print("Search jobs completed, full results saved in CSV files")
