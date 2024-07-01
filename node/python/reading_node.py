import time
import board
import adafruit_sht4x
import requests
import datetime
import argparse
import logging


logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(
        description="Temperature logger"
    )
    parser.add_argument("-n", "--name", action="store", required=True)

    args = parser.parse_args()

    logger.info(f"logging for {args.name}")
    i2c = board.I2C()  # uses board.SCL and board.SDA
    # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
    sht = adafruit_sht4x.SHT4x(i2c)
    logger.info("Found SHT4x with serial number", hex(sht.serial_number))
    
    sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
    # Can also set the mode to enable heater
    # sht.mode = adafruit_sht4x.Mode.LOWHEAT_100MS
    logger.info("Current mode is: ", adafruit_sht4x.Mode.string[sht.mode])
    
    while True:
        temperature, relative_humidity = sht.measurements
        logger.info("Temperature: %0.1f C" % temperature)
        logger.info("Humidity: %0.1f %%" % relative_humidity)

        now = datetime.datetime.now().isoformat()
        logger.info(f"logging at {now}")
    
        try:
            post = requests.post(
                "http://192.168.1.194:8000/api/readings",
                json=dict(
                    time=now,
                    location=args.name,
                    temperature=temperature,
                    humidity=relative_humidity,
                ),
            )
            print(post)
        except Exception as exc:
            logger.exception("Post failed")

        time.sleep(5)
