FROM ubuntu:bionic

ARG DEBIAN_FRONTEND=noninteractive

# PosgreSQL DB
# COPY ./scripts/db.sql /tmp/

# Startup script
# COPY ./scripts/init.sh /

WORKDIR /opt

# Installation
RUN apt-get -qq update \
  && apt-get -yq install --no-install-recommends build-essential patch ruby-bundler ruby-dev zlib1g-dev liblzma-dev git autoconf build-essential libpcap-dev libpq-dev libsqlite3-dev \
    ruby python python3\
    dialog apt-utils \
    python3-msgpack msgpack-python python3-requests  \
  && echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections \
  && git clone https://github.com/trustedsec/unicorn.git \
  && git clone https://github.com/rapid7/metasploit-framework.git \
  && cd metasploit-framework \
  && git fetch --tags \
  && latestTag=$(git describe --tags `git rev-list --tags --max-count=1`) \
  && git checkout $latestTag \
  && rm Gemfile.lock \
  && bundle install \
  && apt-get -y remove --purge build-essential patch ruby-dev zlib1g-dev liblzma-dev git autoconf build-essential libpcap-dev libpq-dev libsqlite3-dev \
  dialog apt-utils \
  && apt-get -y autoremove \
  && apt-get -y clean \
  && rm -rf /var/lib/apt/lists/* \
  # Need to create symbolic link if not unicorn will not work
  && ln -s /opt/metasploit-framework/* /usr/local/bin

# DB config
# COPY ./conf/database.yml /opt/metasploit-framework/config/

# Configuration and sharing folders
# VOLUME /root/.msf4/
# VOLUME /tmp/data/

# Locales for tmux
# ENV LANG C.UTF-8
# WORKDIR /opt/metasploit-framework


# For backconnect shellcodes (payloads)
# EXPOSE 443

# For browser exploits (extra)
# EXPOSE 80
# EXPOSE 8080
# EXPOSE 445
# EXPOSE 8081

#ENTRYPOINT ["/init.sh"]