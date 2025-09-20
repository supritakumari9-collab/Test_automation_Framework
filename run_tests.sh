#!/usr/bin/env bash
set -e
pytest --maxfail=1 -n auto --html=reports/report.html --self-contained-html