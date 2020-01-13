#!/usr/bin/env bash

declare -r py=/usr/bin/python3.8

function init() {
  clear
}

function execute() {
  $py main.py
}

function main() {
  init
  execute
}

main
