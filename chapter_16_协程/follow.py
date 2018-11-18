import time


def follow(thefile):
    thefile.seek(0, 2)
    while True:
        print(1)
        line = thefile.readline()
        print(line)
        if not line:
            time.sleep(0.1)
            continue
        # send line to generator
        yield line


if __name__ == "__main__":

    log_file = open("npm-debug.log")

    for line in follow(log_file):
        print(line)
