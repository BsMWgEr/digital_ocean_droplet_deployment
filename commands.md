# generates secrets for django
python3 -c "import secrets;print(secrets.token_urlsafe(32))"
openssl rand -base64 32
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# Virtual Environment
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate


# django related commands
django-admin startproject <project_name>
python manage.py startapp <app_name>
- or 
django-admin startapp <app_name>
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
python manage.py shell
python manage.py collectstatic --no-input



# ********* postgres related commands **********
# Login into the database Server
ssh root@database.jsquad.app    # add this when needed to specify a key file --> -i ~/.ssh/database
# Change Users
su postgres 
su jon
exit
su root
# Login directly into the database
psql -U postgres -h database.jsquad.app -p 5432
psql -U jon -d post_and_vine -h database.jsquad.app -p 5432

systemctl restart postgresql@14-main.service
systemctl start postgresql@14-main.service
systemctl stop postgresql@14-main.service
systemctl status postgresql@14-main.service

*****************************************************************
****************************************************************
# *******  Add SSL to Postgres related commands  **********

Request a certificate for your server. Replace example.com with the fully-qualified domain name of your server.

sudo certbot certonly --standalone -d example.com


# Create the renewal hook file for ssl cert
sudo nano /etc/letsencrypt/renewal-hooks/deploy/postgresql.deploy

Paste the following. Replace psql.example.com with your server's fully-qualified domain name. Replace the value for DATA_DIR with your PostgreSQL data directory.

******************** copy below here ********************
#!/bin/bash

umask 0177

DOMAIN=psql.example.com

DATA_DIR=/var/lib/postgresql/12/main

cp /etc/letsencrypt/live/$DOMAIN/fullchain.pem $DATA_DIR/server.crt

cp /etc/letsencrypt/live/$DOMAIN/privkey.pem $DATA_DIR/server.key

chown postgres:postgres $DATA_DIR/server.crt $DATA_DIR/server.key

********************   end copy  **************************

# make the file executable
sudo chmod +x /etc/letsencrypt/renewal-hooks/deploy/postgresql.deploy

# Apply the ssl key and cert to the database
# copying the ssl cert and key to the database directory 
cp <ssl_certificate_file> <copy_with_new_location_and_name> # coping to the main directory of postgres where the server.crt and server.key are located and accessible by postgres

cp /etc/letsencrypt/live/database.jsquad.app/fullchain.pem /mnt/volume_nyc3_01/postgresql/14/main/server.crt
cp /etc/letsencrypt/live/database.jsquad.app/privkey.pem /mnt/volume_nyc3_01/postgresql/14/main/server.key

# making the newly copied files executable
chown postgres:postgres /mnt/volume_nyc3_01/postgresql/14/main/server.crt /mnt/volume_nyc3_01/postgresql/14/main/server.key

# show config path file
sudo -u postgres psql -U postgres -c 'SHOW config_file'
# show postgres data dir
sudo -u postgres psql -U postgres -c 'SHOW data_directory'


# Get the path of the PostgreSQL configuration file:

sudo -u postgres psql -U postgres -c 'SHOW config_file'

# Edit the file shown by the previous command. For example:
# replace 14 with the proper version if not 14

sudo nano /etc/postgresql/14/main/postgresql.conf

# Locate the SSL section and edit your file to match these SSL settings:

ssl = on  

ssl_cert_file = 'server.crt'  

ssl_key_file = 'server.key'  

ssl_prefer_server_ciphers = on

# Locate the Connection Settings section and verify the listen_address is to * for all addresses. Make sure the line is not commented out. For example:

listen_address = '*'



# Get the path of the PostgreSQL configuration file:

sudo -u postgres psql -U postgres -c 'SHOW config_file'

# Edit the pg_hba.conf file, which is in the same directory as the configuration file. For example:

sudo nano /etc/postgresql/12/main/pg_hba.conf

# Add the following line to enable secure SSL traffic from the internet.

hostssl all all 0.0.0.0/0 md5

# Optionally, to also allow insecure connections, add the following line:

host all all 0.0.0.0/0 md5

# Save and exit the file.



# Perform a forced renewal, which triggers the Certbot renewal hook to copy the certificates to the correct location for PostgreSQL.

sudo certbot renew --force-renewal

# Look up the PostgreSQL data directory.

sudo -u postgres psql -U postgres -c 'SHOW data_directory'

# Verify that Certbot copied the certs to the PostgreSQL data directory. For example:
# Replace 14 with the proper version if not 14
sudo ls /var/lib/postgresql/12/main/server.*

# Restart PostgreSQL




# *******  docker related commands  **********
docker compose -f docker-compose.prod.yaml --profile app up -d        # --force-recreate
docker compose -f docker-compose.prod.yaml --profile app down
docker compose -f docker-compose.prod.yaml --profile app logs
docker ps
docker compose ps
docker exec -it <container_id> /bin/bash

# terraform related commands

terraform -chdir=./devops/tf init -backend-config=backend
terraform -chdir=./devops/tf validate
terraform -chdir=./devops/tf plan 
terraform -chdir=./devops/tf apply -auto-approve


# ansible related commands
ansible-playbook devops/ansible/main.yaml