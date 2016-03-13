#!/bin/bash

rm /mnt/logs/spider_autohome_`date +%Y%m%d`.out
nohup python main.py > /mnt/logs/spider_autohome_`date +%Y%m%d`.out 2>&1 &
