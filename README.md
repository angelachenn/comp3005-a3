# Compile Instructions
1. Create a database in pgAdmin, and then run the query in `init.sql` to populate your database according to the schema provided in the assignment spec.

2. In `app.py`, please ensure variables:

```
DB_NAME = 'my_database'
DB_USER = 'postgres'
DB_PASSWORD = 'password'
DB_HOST = 'localhost'
DB_PORT = '5432'
```
are configured to your local setup in order to successfully establish a connection to your own postgresql/pgAdmin database from step 2.

3. Run `python app.py` in your terminal in the project directory

Please check what endpoint your Flash server is running on, it should look something like this:
<img width="784" alt="Screenshot 2024-03-19 at 7 11 14 PM" src="https://github.com/angelachenn/comp3005-a3/assets/65053157/bc251797-7e58-4bc2-98e3-6f9ae79ec29a">

4. In `cli_app.py`, please ensure:
   
```
BASE_URL = 'http://127.0.0.1:5000'
```
matches the endpoint from step 3
5. In another terminal window, run `python cli_app.py`

and follow instructions as prompted.

# Demo Video
https://youtu.be/seHPDN2Ryqw
