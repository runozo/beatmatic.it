#!/bin/bash
git archive master | bzip2 >/tmp/source-tree.tar.bz2
scp /tmp/source-tree.tar.bz2 rune@bigdog:/tmp
ssh rune@bigdog 'mkdir /tmp/ttt;cd /tmp/ttt;tar xvjf ../source-tree.tar.bz2;cp -rf /tmp/ttt/* /var/www/beatmatic.it/'
ssh rune@bigdog 'rm -rf /tmp/ttt;rm /tmp/source-tree.tar.bz2'