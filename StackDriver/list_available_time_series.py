'''From https://cloud.google.com/monitoring/custom-metrics/reading-metrics
This example shows how to list only the names and descriptions of the time
 series that match a filter, rather than returning all the available data
'''
from google.cloud import monitoring_v3
import time

project_id = 'valiant-student-208012'
client = monitoring_v3.MetricServiceClient()
project_name = client.project_path(project_id)
interval = monitoring_v3.types.TimeInterval()
now = time.time()
interval.end_time.seconds = int(now)
interval.end_time.nanos = int(
    (now - interval.end_time.seconds) * 10**9)
interval.start_time.seconds = int(now - 300)
interval.start_time.nanos = interval.end_time.nanos
results = client.list_time_series(
    project_name,
    'metric.type = "compute.googleapis.com/instance/cpu/utilization"',
    interval,
    monitoring_v3.enums.ListTimeSeriesRequest.TimeSeriesView.HEADERS)
for result in results:
    print(result)
