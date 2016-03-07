#!/bin/bash

nohup python main.py > nohup_price_`date +%Y%m%d`.out 2>&1 &
