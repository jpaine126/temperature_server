import time
import board
import adafruit_sht4x
import requests
import datetime
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Temperature logger"
    )
    parser.add_argument("-n", "--name", action="store", required=True)

    args = parser.parse_args()

    print(f"logging for {args.name}")
    i2c = board.I2C()  # uses board.SCL and board.SDA
    # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
    sht = adafruit_sht4x.SHT4x(i2c)
    print("Found SHT4x with serial number", hex(sht.serial_number))
    
    sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
    # Can also set the mode to enable heater
    # sht.mode = adafruit_sht4x.Mode.LOWHEAT_100MS
    print("Current mode is: ", adafruit_sht4x.Mode.string[sht.mode])
    
    while True:
        temperature, relative_humidity = sht.measurements
        print("Temperature: %0.1f C" % temperature)
        print("Humidity: %0.1f %%" % relative_humidity)
        print("")
        now = datetime.datetime.now().isoformat()
        print(f"logging at {now}")
    
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
        time.sleep(5)
