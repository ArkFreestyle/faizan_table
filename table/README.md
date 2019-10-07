# Simple HTML Table which displays values as retrieved from database

## Steps to run:

1) Open terminal/cmd

Run the commands: (this is just for setting everything up) 
2) pip install -r requirements.txt
3) python manage.py makemigrations
4) python manage.py migrate

Finally to run the website:
5) python manage.py runserver

Once your server is running, your website should be live at: http://127.0.0.1:8000 or http://localhost:8000

To insert new values into the table, use the URL: http://localhost:8000/values_endpoint/?id=1&num=1&status=on

If you receive an OK http 200 response, then data was added successfully. Refresh your table to view the data.