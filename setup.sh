#!/bin/bash -ex

# update packages
sudo apt-get update
sudo apt-get -y upgrade

# update firmware
sudo rpi-update

# disable services
SERVICES=alsa-restore apt-daily apt-daily-upgrade avahi-daemon dphys-swapfile hciuart nfs-config

sudo systemctl disable ${SERVICES}
sudo systemctl stop ${SERVICES}
sudo systemctl mask ${SERVICES}

# install bluetooth
sudo apt-get -y install bluetooth bluez

# install git
sudo apt-get -y install git

git config --global user.name "Wojciech Holisz"
git config --global user.email "wojciech.holisz@gmail.com"

# install gpio
sudo apt-get -y install i2c-tools wiringpi

# install mongodb
sudo apt-get -y install mongodb

# install python
sudo apt-get -y install python3 python3-pip python3-venv

# install tools
sudo apt-get -y install curl graphviz htop nmap tree vim wget

# install robot
sudo mkdir -p /opt/robot/lib
sudo chown -R pi:pi /opt/robot

python3 -m venv /opt/robot/venv

/opt/robot/venv/bin/pip3 install wheel==0.31.1
/opt/robot/venv/bin/pip3 install pymongo==2.4.2 pyserial==3.4 tornado==5.0.2 wiringpi==2.44.5

git clone https://github.com/pololu/drv8835-motor-driver-rpi.git
/opt/robot/venv/bin/python3 drv8835-motor-driver-rpi/setup.py install

wget https://files.pythonhosted.org/packages/e2/58/6e1b775606da6439fa3fd1550e7f714ac62aa75e162eed29dbec684ecb3e/RPi.GPIO-0.6.3.tar.gz
/opt/robot/venv/bin/pip3 install RPi.GPIO-0.6.3.tar.gz

git clone https://github.com/quick2wire/quick2wire-python-api
cd quick2wire-python-api && /opt/robot/venv/bin/python3 setup.py install && cd ..

git clone https://bitbucket.org/thinkbowl/i2clibraries.git
cp -r i2clibraries /opt/robot/lib/i2clibraries
