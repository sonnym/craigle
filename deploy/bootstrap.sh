#!/usr/bin/env bash

set -e

# system
if [[ ! $(command -v virtualenv) ]]
then
  # system dependencies
  yum install --assumeyes python3-{mod_wsgi,pip} git postgresql-{server,contrib,devel} redis gcc {libxml2,libxslt,python3}-devel supervisor

  # ensure pip3 exists in expected location
  hash pip3 2>/dev/null || ln -s /usr/bin/python3-pip /usr/bin/pip3

  pip3 install virtualenv

  # setup postgresql
  postgresql-setup initdb

  # enable services
  systemctl enable httpd postgresql redis supervisord
  systemctl start postgresql redis

  # set up database and users
  su postgres -c 'createdb craigle_production'
  su postgres -c 'createuser -s root'
  su postgres -c 'createuser -s apache'

  # open port 80
  firewall-cmd --zone=public --add-service=http --permanent && firewall-cmd --reload
fi

# swap file for compiling python binaries
if [[ -n /swapfile ]]
then
  dd if=/dev/zero of=/swapfile bs=1024 count=512k
  mkswap /swapfile
  swapon /swapfile

  echo '/swapfile none swap sw  0 0' >> /etc/fstab

  echo 10 > /proc/sys/vm/swappiness
  echo vm.swappiness = 10 >> /etc/sysctl.conf

  chown root:root /swapfile
  chmod 0600 /swapfile
fi

# application
if [ ! -d /srv/craigle ]
then
  # initial setup of directory
  mkdir -p /srv/craigle
  git clone --depth 1 https://github.com/sonnym/craigle.git /srv/craigle

  cd /srv/craigle

  # add settings files
  if [[ -n craigle/settings.py ]]
  then
    cp craigle/settings.py{.example,}
    echo "SECRET_KEY = '$(openssl rand -base64 32)'" > craigle/secret_key.py
  fi

  # initialize virtualenv
  virtualenv venv

  chown -R apache:apache /srv/craigle
fi

# setup httpd
if [[ -n /etc/httpd/conf.d/craigle.conf ]]
then
  rm /etc/httpd/conf.d/*.conf

  cp /srv/craigle/deploy/httpd.conf /etc/httpd/conf.d/craigle.conf
  systemctl restart httpd
fi

# configure and start workers
if [[ -n /etc/supervisord.d/craigle_worker.ini ]]
then
  cp /srv/craigle/deploy/supervisord.ini /etc/supervisord.d/craigle_worker.ini
  systemctl start supervisord
fi

# configure sshd
if [[ -n $(diff /srv/craigle/deploy/sshd_config /etc/ssh/sshd_config) ]]
then
  cp /srv/craigle/deploy/sshd_config /etc/ssh/sshd_config
  chown root:root /etc/ssh/sshd_config
  systemctl restart sshd
fi
