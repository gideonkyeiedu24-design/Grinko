# Import the necessary libraries
import sqlite3  # This library helps us interact with SQLite databases
import csv  # This library helps us read and write CSV files

# Define some constants to make our code easier to read and maintain
DATABASE_NAME = "grinko.db"  # The name of our SQLite database
TABLE_NAME = "faults"  # The name of the table we're creating
CSV_FILE_NAME = "fault_data.csv"  # The name of the CSV file we're importing

# Define the schema for our table
TABLE_SCHEMA = """
CREATE TABLE IF NOT EXISTS faults (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symptom TEXT,
    cause TEXT,
    checks TEXT
)
"""

# Function to create the table if it doesn't exist
def create_table(conn):
    """
    Create the faults table if it doesn't exist.

    Args:
        conn (sqlite3.Connection): The connection to our SQLite database.
    """
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Execute the SQL query to create the table
    cursor.execute(TABLE_SCHEMA)

# Function to import data from the CSV file into the faults table
def import_csv_data(conn, csv_file_name):
    """
    Import data from the CSV file into the faults table.

    Args:
        conn (sqlite3.Connection): The connection to our SQLite database.
        csv_file_name (str): The name of the CSV file we're importing.
    """
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Open the CSV file and read its contents
    with open(csv_file_name, newline='', encoding="utf-8-sig") as file:
        # Create a DictReader object to read the CSV file
        reader = csv.DictReader(file)
        # Iterate over each row in the CSV file
        for row in reader:
            # Execute the SQL query to insert the row into the table
            cursor.execute("""
            INSERT INTO faults (symptom, cause, checks)
            VALUES (?, ?, ?)
            """, (row["Symptoms"], row["Probable Cause(s)"], row["What Mechanic Checks"]))

# Main function to orchestrate the entire process
def main():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DATABASE_NAME)
        # Create the table if it doesn't exist
        create_table(conn)
        # Import data from the CSV file into the faults table
        import_csv_data(conn, CSV_FILE_NAME)
        # Save the changes to the database
        conn.commit()
        # Print a success message
        print("Data imported successfully.")
    except sqlite3.Error as e:
        # Print an error message if something goes wrong
        print(f"Error: {e}")
    finally:
        # Close the connection to the database
        if 'conn' in locals():
            conn.close()

# Call the main function if this script is run directly
if __name__ == "__main__":
    main()