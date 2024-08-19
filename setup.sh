#!/bin/bash

# homebrewがない場合インストール
if !(type "brew" > /dev/null 2>&1); then
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  brew install python3 sqlite
fi

# Python仮想環境がない場合作成
if [ ! -d ./venv ]; then
  python3 -m venv venv
fi

if [ -z "$VIRTUAL_ENV" ]; then
  source ./venv/bin/activate
fi

# 依存パッケージのインストール
pip install -r requirements.txt
