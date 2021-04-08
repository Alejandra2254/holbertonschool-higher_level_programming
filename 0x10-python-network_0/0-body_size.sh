#!/bin/bash
# Script that takes URL, sen a requesr and display size
url_to_use=$1
curl -so /dev/null "$url_to_use" -w %'{size_download}\n'