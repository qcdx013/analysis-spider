#!/bin/bash

nohup python main.py > /mnt/logs/spider/nohup_price_`date +%Y%m%d`.out 2>&1 &
