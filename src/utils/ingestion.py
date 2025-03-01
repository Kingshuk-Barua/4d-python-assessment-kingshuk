
from src.configs.file_configs import CONFIGS
from src.utils.watermark import get_watermark_table, update_watermark_table, get_last_run_date
from src.utils.files import get_read_func, get_files_to_process, get_file_date
from src.utils.dataframes import process_data
from src.utils.logger import sys_logger

def run_ingestion():
    watermark_table = get_watermark_table()

    for source_name, config in CONFIGS.items():
        if source_name == "error":
            continue
        sys_logger.info(f"Loading {source_name} data")
        read_func = get_read_func(config['file_type'])
        last_run_date = get_last_run_date(source_name, watermark_table)
        location = config['location']
        files_to_process = get_files_to_process(location, last_run_date)
        sorted_files = sorted(files_to_process)
        for file in sorted_files:
            sys_logger.info(f"Processing {file}")
            date = get_file_date(file)
            df = read_func(location + file, **config.get('read_args', {}))
            stats = process_data(source_name, df, config, date)
            stats['file_name'] = file
            watermark_table = update_watermark_table(watermark_table, stats)
            sys_logger.info(f"Processed {file}")