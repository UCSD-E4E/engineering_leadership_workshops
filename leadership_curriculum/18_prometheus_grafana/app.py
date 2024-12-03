from prometheus_client import start_http_server, Summary, Gauge, Info
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
class App:
    def __init__(self):
        self.__value = 0
        self.APP_VALUE = Gauge('application_value', 'Application value')
        self.APP_VALUE.set_function(lambda: self.__value)

        Info('app_version', 'Application version').info({'version': '0.0.1', 'hostname': 'foobar'})

        self.binned_gauge = Gauge('binned_application_value', 'Binned App Value', labelnames=['bin'])


    # Decorate function with metric.
    @REQUEST_TIME.time()
    def process_request(self, t):
        """A dummy function that takes some time."""
        self.__value += t
        # with REQUEST_TIME.time():
        self.binned_gauge.labels(bin=f'{int(t * 10)}').inc()
        time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(9092)
    # Generate some requests.
    app = App()
    while True:
        app.process_request(random.random())
