# Azure JSON Feeder

Azure JSON Feeder is a Python application that efficiently processes JSON data and stores it into an Azure SQL Database. It provides a streamlined workflow for configuring the database connection, defining database models, processing JSON data, and initiating the data ingestion process.

## Usage

1. **Configuration**: Set up your environment by creating a `.env` file with your Azure SQL Database connection URL. Refer to `config.py` for configuration management.

2. **Database Setup**: Use `database.py` to establish a connection to your Azure SQL Database using SQLAlchemy. Ensure that the database schema aligns with the defined models in `models.py`.

3. **JSON Processing**: Utilize `json_processor.py` to parse JSON data and insert it into the database. Adjust the JSON parsing logic as needed to match your data structure.

4. **Data Ingestion**: Execute `main.py` to initiate the data ingestion process. Specify the path to your JSON file to begin processing.

5. **Testing (Optional)**: Test your database models using the tests provided in the `tests` directory. Ensure data integrity and model functionality with comprehensive testing.

