import logging

# log level
# 1. debug
# 2. info
# 3. warning
# 4. error
# 5. critical

# print(logging.getLogger())#<RootLogger root (WARNING)>
# lg=logging.getLogger()
# lg.setLevel(logging.DEBUG)
# print(logging.getLogger())

### to get log in file
# logging.basicConfig(filename="./file1.log", filemode="a",
#                     format="%(asctime)s::%(levelname)s::%(message)s",
#                     level=logging.DEBUG)

### to get log in console and file

logging.basicConfig(handlers=[logging.StreamHandler(),
                              logging.FileHandler(filename="./file2.log", mode="a")],
                    format="%(asctime)s::%(levelname)s::%(message)s",level=logging.DEBUG)


logging.debug("this is debug msg")
logging.info("this is info msg")
logging.warning("this is warn msg")
logging.error("this is error msg")
logging.critical("this is critical msg")
