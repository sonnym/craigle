#!/usr/bin/env bash

# upgrade to fedora 21
if [[ $(cat /etc/fedora-release) == "Fedora release 20 (Heisenbug)" ]]
then
  yum --assumeyes update
  rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-21-$(uname -i)
  yum --assumeyes update yum
  yum --assumeyes clean all
  yum --releasever=21 --assumeyes distro-sync
  yum --assumeyes remove firewalld-config-standard
  yum --assumeyes install system-release-server

  sync

  PROVISION_REBOOT=!
fi

if [[ ! $(command -v virtualenv) ]]
then
  # system dependencies
  yum install --assumeyes python3-mod_wsgi git postgresql-{server,contrib,devel} redis gcc {libxml2,libxslt,python3}-devel
  pip3 install virtualenv

  # setup postgresql
  postgresql-setup initdb

  # enable services
  systemctl enable httpd postgresql redis
  systemctl start httpd postgresql redis

  # set up database and users
  su postgres -c 'createdb craigle_production'
  su postgres -c 'createuser -s root'
  su postgres -c 'createuser -s apache'
fi

if ! [ -L /srv/craigle ]
then
  # initial setup of directory
  mkdir -p /srv/craigle
  chown -R apache:apache /srv
  git clone --depth 1 https://github.com/sonnym/craigle.git /srv/craigle

  cd /srv/craigle

  # add settings files
  if [[ -n /srv/craigle/craigle/settings.py ]]
  then
    cp /vagrant/craigle/settings.py.example craigle/settings.py
    echo "SECRET_KEY = '$(openssl rand -base64 32)'" > craigle/secret_key.py
  fi

  # local dependencies
  virtualenv venv
  source venv/bin/activate
  pip3 install -r requirements.txt

  # migrations, static files, admin, and initial queue function
  ./manage.py migrate

  ./manage.py collectstatic --noinput
  ./manage.py createsuperuser --noinput --email=michaud.sonny@gmail.com --username=sonny

  ./manage.py rqenqueue 'importers.run'
fi

if [[ -n /etc/httpd/conf.d/craigle.conf ]]
then
  # setup httpd
  rm /etc/httpd/conf.d/*.conf
  cp /vagrant/deploy/httpd.conf /etc/httpd/conf.d/craigle.conf
fi

if [[ $PROVISION_REBOOT ]];
then
  /sbin/shutdown -r now
fi
