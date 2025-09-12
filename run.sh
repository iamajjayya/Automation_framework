#!/bin/bash
# This script runs all your tests inside Docker

pytest -s -v --html=./Reports/report.html testCases/ --browser chrome
