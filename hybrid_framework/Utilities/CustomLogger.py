import logging
import datetime

def customlog():
    log_path=r"C:\Users\user\PycharmProjects\pythonProject_WE_MARCH\hybrid_framework\Logs"
    dt = datetime.datetime.now().strftime("%d_%m_%y_%H%M%S")
    logging.basicConfig(handlers=[logging.StreamHandler(),
                                  logging.FileHandler(filename=fr"{log_path}\log_{dt}.txt", mode="w")],
                        format="%(asctime)s::%(levelname)s::%(message)s", level=logging.INFO,
                        force=True
                        )
    return logging