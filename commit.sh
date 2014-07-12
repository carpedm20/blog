#!/usr/bin/env bash
##
# This section should match your Makefile
##
cp -r ../old_carpedm20.github.com/solar ./output/
cp -r ../old_carpedm20.github.com/ndrive ./output/
cp -r ../old_carpedm20.github.com/randomwall ./output/
pelican content; cd output/; git add .; git commit -m "neural-network-translation update"; git push origin master; cd -
