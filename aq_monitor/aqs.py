import pprint
import time
from datetime import datetime

from sds011 import SDS011


def measure_pm25():
    sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
    reading = sensor.query()
    return {"pm2.5": reading[0], "pm10": reading[1]}


if __name__ == "__main__":
    data = dict()
    for i in range(10):
        data[datetime.strftime(datetime.now(), "%Y%m%dT:%H:%M:%S.%f")] = measure_pm25()
        time.sleep(1)
    pprint.pprint(data)
