DjangoWebsite
=============
The Umonya Website written in Django.

In order to run the site the database needs to be created and upoaded with the JSON data, failure to do so means that some of the pages will be broken.

Start up Database and Load Data
===============================
Run the following commands in the shell/command prompt
 - python manage.py syncdb
 - python manage.py loaddata umonya/umonya/apps/main/fixtures/main.json