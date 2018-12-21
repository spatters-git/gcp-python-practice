'''
from https://cloud.google.com/monitoring/custom-metrics/reading-metrics
This example returns all the information available to the timeSeries.list request,
 including the metric data, from Compute Engine instances for the last 20 minutes.
'''

from google.cloud import monitoring_v3
import time
import os
import json

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
    monitoring_v3.enums.ListTimeSeriesRequest.TimeSeriesView.FULL)


for result in results:
    print("Full result")
    print(result)
    print("Extracting the instance name:")
    print(result.metric.labels.get('instance_name'))
    print("Extracting the value from the first metric point in the time series:")
    print(result.points[0].value.double_value)







