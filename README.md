# Robot

Robot based on Raspberry Pi Zero.

## Configuration

### GPIO

```
 5 - motor direction (left)
 6 - motor direction (right)
12 - motor speed (left) 
13 - motor speed (right)
18 - servo
16 - encoder (left)
21 - encoder (right)
```

### Raspberry Pi Zero

Install Raspbian and configure `/boot/config.txt` file:

```
dtparam=i2c_arm=on
dtparam=spi=off
enable_uart=1
gpu_mem=128
start_x=1
```

Run `setup.sh`.

## Parts

- https://botland.com.pl/podwozia-robotow/7283-chassis-rectangle-2wd-2-kolowe-podwozie-robota-z-napedem.html
- https://botland.com.pl/moduly-i-zestawy-raspberry-pi-zero/8330-raspberry-pi-zero-w-512mb-ram-wifi-bt-41.html
- https://botland.com.pl/raspberry-pi-hat-kontrolery-silnikow-i-serw/2678-pololu-drv8835-dwukanalowy-sterownik-silnikow-11v12a-nakladka-dla-raspberry-pi.html
- https://botland.com.pl/przetwornice-step-up-step-down/941-pololu-s7v7f5-przetwornica-step-upstep-down-5v-1a.html
- https://botland.com.pl/transoptory-odbiciowe/8834-waveshare-czujnik-szczelinowy.html
- https://botland.com.pl/serwa-praca-ciagla-360/4689-serwo-feetech-fs90r-micro-praca-ciagla-360-stopni.html
- https://botland.com.pl/skanery-laserowe/10198-laserowy-czujnik-odleglosci-lidar-tfmini-uart-12m.html
- https://botland.com.pl/magnetometry/9412-magnetometr-gy-273-3-osiowy-cyfrowy-i2c-33v-5v-hmc5883l-qmc5883.html
- https://botland.com.pl/konwertery-napiec/2523-konwerter-poziomow-logicznych-dwukierunkowy-czterokanalowy-pololu.html
