## website is website

- django-tenant-schemas

#### Schema structure

- public shared
- website
- private

#### Credentials
user: admin
pass: admin

#### Data
- Dump data `./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json`
- `./manage.py loaddata db.json`
- `django-tenant-schemas` need to be set up. Also exclude  django-tenant-schema's data before dump. Loaddata does not support it because it need migration.


#### Instructions:
https://github.com/vimm0/auto-script#django-tenant
