#!/usr/bin/env bash

set -e
set -x

coverage run manage.py test  && coverage report -m "${@}"
