import pandas as pd
from src.configs.schemas import SCHEMAS
from src.utils.logger import sys_logger
from datetime import datetime



def validate_data(source_name, dataframe):
    """Performing data validation"""

    try:
        schema = SCHEMAS[source_name]
    except KeyError:
        sys_logger.warning(f"No schema found for {source_name}")
        return dataframe, pd.DataFrame(columns=dataframe.columns)
    
    error_rows = pd.DataFrame(columns=dataframe.columns)
    clean_rows = pd.DataFrame(columns=dataframe.columns)

    for _, row in dataframe.iterrows():
        row_dict = row.to_dict()
        has_error = False

        for field_info in schema:
            field = field_info["name"]
            expected_type = field_info["type"]
            required = field_info.get("required", False)
            valid_values = field_info.get("values", [])
            
            if required and field not in row_dict:
                has_error = True
                sys_logger.warning(f"Missing Required Field: {field}")
                break
            
            value = row_dict.get(field)

            if (value is None or value == "" or pd.isna(value)):
                if required:
                    has_error = True
                    sys_logger.warning(f"Missing Required Field: {field}")
                    break
                else:
                    continue
            
            if expected_type == "int":
                if not isinstance(value, int):
                    has_error = True
                    sys_logger.warning(f"Expected {field} to be int, got {value} of type {type(value)}")
                    break                
            elif expected_type == "float":
                if not isinstance(value, (float, int)):  # Allowing int for float fields
                    has_error = True
                    sys_logger.warning(f"Expected {field} to be float, got {value} of type {type(value)}")
                    break                    
            elif expected_type == "string":
                if not isinstance(value, str):
                    has_error = True
                    sys_logger.warning(f"Expected {field} to be string, got {value} of type {type(value)}")
                    break                    
            elif expected_type == "enum":
                if value not in valid_values:
                    has_error = True
                    sys_logger.warning(f"Incorrect values for {field}. Expected {valid_values}, got {value}")
                    break    

            elif expected_type == "date":
                date_format = field_info["format"]
                try:
                    datetime.strptime(value, date_format)
                except ValueError:
                    has_error = True
                    sys_logger.warning(f"Incorrect date formt. Received date as {value}, expected format {date_format}")
                    break    
                        
        if has_error:
            error_rows = pd.concat([error_rows, row.to_frame().T], ignore_index=True)
        else:
            clean_rows = pd.concat([clean_rows, row.to_frame().T], ignore_index=True)

    return clean_rows, error_rows