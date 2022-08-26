# test-arcane

To run the app, use the following command

==> pip install -r requirements.txt

==> python3 app.py

You can then test the features on Postman :

GET http://127.0.0.1:5000/users

GET http://127.0.0.1:5000/users/<user_id>

POST http://127.0.0.1:5000/users

Json input:
{
"first_name":"first name",
"last_name":"last name",
"date_birth": "05/11/1990"
}


PUT http://127.0.0.1:5000/users/<user_id>
