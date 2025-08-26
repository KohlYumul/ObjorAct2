# ObjorAct2

Instructions for Cloning the Project

1. Run the command in the terminal

   git clone https://github.com/KohlYumul/ObjorAct2
   
   cd ObjorAct2

3. Also run these commands to prevent first run errors

     python manage.py makemigrations

     python manage.py migrate

4. Create a superuser:
   
     python manage.py createsuperuser

5. Start the development server:

     python manage.py runserver

6. Login using the superuser account you created

7. Post a tweet and click "Go to Admin Page to see Tweets and History" to view the history and tweet you created
Now, go back to http://127.0.0.1:8000/ and post a tweet.

After posting, you can check the admin page again to see the new Tweet and the corresponding History object that was created automatically by the signal.



