#!/bin/bash
gunicorn myshop.wsgi --bind 0.0.0.0:$PORT
