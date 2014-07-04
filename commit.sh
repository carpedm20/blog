#!/usr/bin/env bash
##
# This section should match your Makefile
##
pelican content; cd output/; git add .; git commit -m "neural-network-translation update"; git push origin master; cd -
