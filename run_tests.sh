#!/bin/sh
rm -rf allure-results
python -m behave
allure serve
