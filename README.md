## website is website

- django-tenant-schemas

#### Tips
- Never place `'django.contrib.auth'` in shared_apps instead place at tenant_app
#### Schema structure

- public shared
- tenant

#### Schema Format
```
#   Domain Name             schema  Organization Name
--------------------------------------------------------
1	nepexgroup.com	        website	Nepex Group
2	client1.nepexgroup.com	client1	Client1 Organization
3	client2.nepexgroup.com	client2	Client2 Organization

```

#### Authentication Format
```
schema  user  password
-----------------------
website admin admin
client1 client1 admin
client2 client2 admin
```

#### Data
- Dump data `./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json`
- `./manage.py loaddata db.json`
- `django-tenant-schemas` need to be set up. Also exclude  django-tenant-schema's data before dump. Loaddata does not support it because it need migration.


#### Instructions:
https://github.com/vimm0/auto-script#django-tenant


#### Tags
- [feature not supported]
