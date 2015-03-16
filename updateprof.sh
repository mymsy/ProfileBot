#!/bin/bash

#
# Wrapper script for ProfileBot. 
# Replace the dummy value with your own API keys, from apps.twitter.com,
# and your preferred profile message.
#

python profilebot.py --consumer_key $CK \
                     --consumer_secret $CS \
                     --access_token $AT \
                     --access_token_secret $ATS \
                     --profile "This is a adjective message!" \
                     --replace "adjective" \
                     --with "profile" "ridiculous" "silly" "ebooks" "annoying"
