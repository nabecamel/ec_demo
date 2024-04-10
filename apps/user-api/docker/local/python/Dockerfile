FROM python:3.10

# 必要なものをインストール
RUN apt-get update
RUN apt-get -y install locales

# 日本語設定
RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

# デフォルトのディレクトリを設定
# イメージにディレクトリがないので作成される
WORKDIR /app

# project配下に.venvを作成する
ENV PIPENV_VENV_IN_PROJECT=1

# log出力をリアルタイムにする
ENV PYTHONUNBUFFERED=1

# キャッシュを作成しない
ENV PYTHONDONTWRITEBYTECODE=1

# パスを通す
ENV PYTHONPATH "/app"

# デバッグ用
EXPOSE 9000

# pipのアップデート
RUN pip install --upgrade pip

# pipenvのインストール
RUN pip install --upgrade setuptools pipenv

# プロジェクトをappにコピー
COPY ./ /app/

# ライブラリのインストール
RUN pipenv install --dev
