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


#### Instructions:
https://github.com/vimm0/auto-script#django-tenant
