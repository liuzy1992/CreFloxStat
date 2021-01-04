#!/usr/bin/env bash

find "$1" -name '*.txt' | parallel -j "$2" ./main.sh
