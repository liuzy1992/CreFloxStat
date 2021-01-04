#!/usr/bin/env bash

tmpfile1=$(mktemp -u)
tmpfile2=$(mktemp -u)
filename=$(basename $1)
id=${filename%.txt}
../bitbucket/cre-floxminingtool/iconv/iconv.sh "$1" > "$tmpfile1"
../bitbucket/cre-floxminingtool/sentSegmentAndTokenize/sentSegmentAndTokenize.py "$id" "$tmpfile1" > "$tmpfile2"
./CreFloxStat.py "$tmpfile2"
