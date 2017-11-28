#!/bin/bash
# Deletes non-useful files.
find . -name "*.pyc" -type f -delete
find . -name "*.DS_Store" -type f -delete
ls -lh
