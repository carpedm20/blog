#!/usr/bin/env bash
##
# This section should match your Makefile
##
#cp -r ../old_carpedm20.github.com/solar ./output/
#cp -r ../old_carpedm20.github.com/ndrive ./output/
#cp -r ../old_carpedm20.github.com/randomwall ./output/
pelican content; git add .; git commit -m "blog update"; git push origin master;
echo "cp -r ./output/* ../carpedm20.github.io/"
echo "cd ../carpedm20.github.io"
echo "cp ./about/index.html ."
echo "git add ."
echo "git commit -m 'blog update'"
echo "git push origin master"
