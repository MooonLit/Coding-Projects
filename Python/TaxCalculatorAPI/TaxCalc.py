# Importing the Flask framework and necessary modules
import flask
from flask import jsonify
from flask import request
import creds
from sql import create_connection
from sql import execute_read_query
from sql import execute_query


# Initializing a Flask application
app = flask.Flask(__name__)
app.config["Debug"] = True
#change line 15
# Route to handle GET requests for viewing Tax amount based on a valid user given state and the amount the want to be taxed in the header of postman API
@app.route('/api/calculate', methods=['GET'])
def calculate_tax():
        #LIne 19 and 20 Chatgpt Helped me with this
        NewCode = request.headers.get('state')
        Amount = request.headers.get('amount')
        myCreds = creds.Creds()
        conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.database)
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM Taxes"
        cursor.execute(sql)
        All_Products = cursor.fetchall()
        total = 0
        for row in All_Products:
            if row['state'] == NewCode:
                total = row['taxrate'] * int(Amount)
        if total == 0:
            return 'Error Occured'
        else:
            #line 35 from chatgpt
            return '$' + str(total)


# Route to handle POST requests for adding a tax entry.
@app.route('/api/tax', methods=['POST'])
def add_new_tax_entry():
    request_data = request.get_json()
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.database)
    NewStateCode = request_data['state']
    NewRate = request_data['taxrate']
    


    # Define SQL query to insert a new tax entry
    sql = ("INSERT INTO Taxes(state, taxrate) VALUES "
           "('%s', '%s')") % (NewStateCode, NewRate)

    # Execute the SQL query
    execute_query(conn, sql)
    return 'Add request successful!'

# Route to handle DELETE requests for deleting a tax entry from the data base
@app.route('/api/tax', methods=['DELETE'])
def delete_tax_entry():
    id_to_delete = request.args['state']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.database)
    
    # Define SQL query to delet a tax entry
    #line 65 from chatgpt
    sql = ("DELETE FROM Taxes WHERE state = '%s'" % id_to_delete)
    execute_query(conn, sql)
    return 'Successfully Deleted!'

# Running the Flask application
app.run()