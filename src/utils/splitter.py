import re
from src.configs.file_configs import CONFIGS
import shutil
import os
from src.utils.logger import sys_logger

def split_files():
    new_files = os.listdir('./landing_zone/')
    sys_logger.info(f"Files in landing zone: {new_files}")
    for file in new_files:
        for source_name, config in CONFIGS.items():
            if source_name == "error":
                continue
            pattern = config['file_pattern']
            if re.match(pattern, file):
                sys_logger.info(f"{file} matched with {source_name}")
                os.makedirs(name=config['location'], exist_ok=True)
                shutil.move(f"./landing_zone/{file}", f"{config['location']}{file}")
                sys_logger.info(f"{file} moved to {config['location']}")
                break
        else:
            sys_logger.warning(f"{file} did not match with any source")