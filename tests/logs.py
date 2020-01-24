import logging
import os


formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.FileHandler(os.path.join(os.pardir, __name__))
logs = logging.getLogger(__name__)

handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logs.addHandler(handler)
