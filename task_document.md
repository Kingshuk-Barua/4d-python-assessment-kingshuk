# Tasks Completed

## a. Ran the workbook.ipynb notebook

The first report successfully matched customer_growth.png.
As expected, the second report failed due to an issue in the pipeline.

## b. Fixed the Sales Pipeline

Identified and corrected mistakes throughout the pipeline without adding new lines of code.
Had to just make changes in src/configs/file_configs.py and
successfully got the second report to work, matching sales_by_membership.png.

## c. Implemented the Product Pipeline

Integrated JSON files into the ingestion pipeline following the same patterns as the other two pipelines.
Created a configuration in ./src/configs/file_configs.py to use PRODUCT_SCHEMA from ./src/configs/schemas.py and
define other relevant configurations for the product pipeline. Added a condition in src/utils/files.py to handle the reading of json files, since products data are available in json format.
Successfully generated the third report as a dataframe, which matched product_sale_breakdown.csv.

## d. Completed Two Tickets

### Ticket MIDP-307
 - Generated 2 csv reports containing the following details
    1. The top 10 people who purchased the largest number of products.
    2. The top 10 people who purchased the largest number of products while being an active member.

 - Since this is a one time adhoc requirement by the client, I have added a code cell in workbook.ipynb which reads the required data from the customer.parquet and sales.parquet files, and provides with the required reports.

 #### Note:
 While doing this task, I noticed that if the data for a customer does not come daily, we are making the is_current as False. For such customer_ids, there is no row for is_current=True. As per my understanding, atleast 1 row containing is_current=True should be there for each customer_id, because is_current field helps us understand if the data is latest or historical. Also, there is no provision for deleted custoemrs. There should be a column for is_deleted in 
 products.parquet and customers.parquet where we can control, whether the data exists any longer or not, instead of deleting the data directly from the database. This will help us preserve every sort of historical data.

### Ticket MIDP-313 – 
Modified and completed the placeholder code in ./src/utils/validation.py, using the schemas from ./src/configs/schemas.py.
In the validation logic, I have implemented the following - 
1. Checked if any field having 'required' = True, is missing or not. If any required value is missing, it is an error.
2. Checked if the datatype of the value is matching the required datatype from the schema.
3. Checked if the 'enum' fields, contain valid values or not.
4. Checked if the 'date' fields contain the date format specified in the schema or not.