#!/bin/bash

if [ -z "$VIRTUAL_ENV" ]; then
  source ./venv/bin/activate
fi

# 依存パッケージのインストール
pip install -r requirements.txt
