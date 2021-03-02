from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime

class StoreData:
    def __init__(self, url, org, token):
        self.url = url
        self.org = org
        self.token = token
        self.client = InfluxDBClient(url=url, token=token)

    def insert_data(self, bucket, point):
        write_api = self.client.write_api(write_options=SYNCHRONOUS)

        result = write_api.write(bucket, self.org, point)

    def delete_data(self, start, stop, measurement, type_tag, bucket):
        delete_api = self.client.delete_api()
        start_date = "1970-01-01T00:00:00Z"
        stop_date = "2099-12-01T00:00:00Z"

        if start:
            start_date = start
        
        if stop:
            stop_date = stop

        predicate = '_measurement="{}" and type="{}"'.format(measurement, type_tag)


        delete_api.delete(start_date, stop_date, predicate, bucket=bucket, org=self.org)

        return True