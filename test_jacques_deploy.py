import logging
import time


def main():
    logging.basicConfig(level=logging.INFO)
    while True:
        logging.info("ça marche")
        time.sleep(3)


if __name__ == "__main__":
    main()
