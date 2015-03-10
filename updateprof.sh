#!/bin/bash

python profilebot.py --consumer_key $CK \
					 --consumer_secret $CS \
                     --access_token $AT \
                     --access_token_secret $ATS \
                     --profile "This is a adjective message!" \
                     --replace "adjective" \
                     --with "profile" "ridiculous" "silly" "ebooks" "annoying"
