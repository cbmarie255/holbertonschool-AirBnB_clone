# 0x00. AirBnB clone - The console
## Tasks
###  README, AUTHORS

###  Be PEP8 compliant!

###  Unittests
All your files, classes, functions must be tested with unit tests.
### 4. BaseModel

Write a class  `BaseModel`  that defines all common attributes/methods for other classes: `models/base_model.py`

 -   Public instance attributes:
    -   `id`: string - assign with an  `uuid`  when an instance is created:
        -   you can use  `uuid.uuid4()`  to generate unique  `id`  but don’t forget to convert to a string
        -   the goal is to have unique  `id`  for each  `BaseModel`
    -   `created_at`: datetime - assign with the current datetime when an instance is created
    -   `updated_at`: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
  
### 5. Create BaseModel from dictionary
Update  `models/base_model.py`:
`__init__(self, *args, **kwargs)`
### 6. Store first object
 - Write a class  `FileStorage`  that serializes instances to a JSON file and deserializes JSON file to instances:
`models/engine/file_storage.py`
 - Update `models/__init__.py`: to create a unique `FileStorage` instance for your application
 - Update `models/base_model.py`: to link your `BaseModel` to `FileStorage` by using the variable `storage`
### 7. Console 0.0.1

Write a program called  `console.py`  that contains the entry point of the command interpreter.
### 8. Console 0.1

Update your command interpreter (`console.py`) to have these commands:

 - `create`: Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. Ex: `$ create BaseModel`
 - `show`: Prints the string representation of an instance based on the class name and `id`. Ex: `$ show BaseModel 1234-1234-1234`
 - `destroy`: Deletes an instance based on the class name and `id` (save the change into the JSON file). Ex: `$ destroy BaseModel 1234-1234-1234`
 - `all`: Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel`or `$ all`
 - `update`: Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`
 ### 9. First User

Write a class  `User`  that inherits from  `BaseModel`:
-   Public class attributes:
    -   `email`: string - empty string
    -   `password`: string - empty string
    -   `first_name`: string - empty string
    -   `last_name`: string - empty string

Update  `FileStorage`  to manage correctly serialization and deserialization of  `User`.
### 10. More classes!

Write all those classes that inherit from  `BaseModel`:

-   `State`  (`models/state.py`):
    -   Public class attributes:
        -   `name`: string - empty string
-   `City`  (`models/city.py`):
    -   Public class attributes:
        -   `state_id`: string - empty string: it will be the  `State.id`
        -   `name`: string - empty string
-   `Amenity`  (`models/amenity.py`):
    -   Public class attributes:
        -   `name`: string - empty string
-   `Place`  (`models/place.py`):
    -   Public class attributes:
        -   `city_id`: string - empty string: it will be the  `City.id`
        -   `user_id`: string - empty string: it will be the  `User.id`
        -   `name`: string - empty string
        -   `description`: string - empty string
        -   `number_rooms`: integer - 0
        -   `number_bathrooms`: integer - 0
        -   `max_guest`: integer - 0
        -   `price_by_night`: integer - 0
        -   `latitude`: float - 0.0
        -   `longitude`: float - 0.0
        -   `amenity_ids`: list of string - empty list: it will be the list of  `Amenity.id`  later
-   `Review`  (`models/review.py`):
    -   Public class attributes:
        -   `place_id`: string - empty string: it will be the  `Place.id`
        -   `user_id`: string - empty string: it will be the  `User.id`
        -   `text`: string - empty string
### 11. Console 1.0

Update  `FileStorage`  to manage correctly serialization and deserialization of all our new classes:  `Place`,  `State`,  `City`,  `Amenity`  and  `Review`

Update your command interpreter (`console.py`) to allow those actions:  `show`,  `create`,  `destroy`,  `update`  and  `all`  with all classes created previously.


