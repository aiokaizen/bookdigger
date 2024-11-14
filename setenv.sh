#!/bin/bash

export BASE_DIR=$(pwd)
export DJANGO_SETTINGS_MODULE='bookdigger.settings'
export VENV_DIR=$BASE_DIR/venv

source $VENV_DIR/bin/activate
