# test-arcane

To run the app, use the following command

==> pip install -r requirements.txt

==> python3 app.py

You can then test the features on Postman :

To get all the users : 

GET http://127.0.0.1:5000/users

To get a specific user : 

GET http://127.0.0.1:5000/users/<user_id>

To create an user : 

POST http://127.0.0.1:5000/users

Then go to Body => Raw => Json and create a JSon with following parameters :

{

"first_name":"",

"last_name":"",

"date_birth": ""

}

To update an user : 

PUT http://127.0.0.1:5000/users/<user_id>

Then go to Body => Raw => Json and create a JSon with following parameters :

{

"first_name":"",

"last_name":"",

"date_birth": ""

}

To add a property : 

POST http://127.0.0.1:5000/properties/<user_id>

Then go to Body => Raw => Json and create a JSon with following parameters :


{

"name":"",

"description":"",

"type":"",

"city":"",

"rooms": ,

"char_rooms":""

}

To get property by city :

GET http://127.0.0.1:5000/properties?city=city_name

To update a property : 

PUT  http://127.0.0.1:5000/properties/<user_id>/<product_id>

Then go to Body => Raw => Json and create a JSon and update the parameters with the same format as when you create it 
