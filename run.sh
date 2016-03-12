#!/bin/bash

nohup python main.py > /mnt/logs/spider_auto_`date +%Y%m%d`.out 2>&1 &
