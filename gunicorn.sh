#!/bin/sh
gunicorn app:app -w 5 --threads 2 -b 0.0.0.0:5000