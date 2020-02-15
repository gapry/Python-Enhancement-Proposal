#!/usr/bin/env bash

declare -r py=/usr/bin/python3.8
declare -r app=main.py

clear
bat $app
$py $app
