
  - virtualenv virtenv
  - source virtenv/bin/activate
  - pip install -r docs/requirements.txt


  - #db под гитом (db_1_9_8.sqlite3), admin@superadmin
  - #python manage.py syncdb
  - #python manage.py migrate
