#!/usr/bin/env bash
##
# This section should match your Makefile
##
#cp -r ../old_carpedm20.github.com/solar ./output/
#cp -r ../old_carpedm20.github.com/ndrive ./output/
#cp -r ../old_carpedm20.github.com/randomwall ./output/
pelican content; git add . --all; git commit --amend; git push -f origin master;
echo "cp -r ./output/* ../carpedm20.github.com/"
echo "cd ../carpedm20.github.com"
echo "cp ./about/index.html ."
echo "git add ."
echo "git commit -m 'update'"
echo "git push origin master"
