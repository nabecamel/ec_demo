FROM python:3.10

RUN apt-get update
RUN apt-get -y install locales
RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

WORKDIR /app

# project配下に.vnvを作成する
ENV PIPENV_VENV_IN_PROJECT=1

# log出力をリアルタイムにする
ENV PYTHONUNBUFFERED=1

# キャッシュを作成しない
ENV PYTHONDONTWRITEBYTECODE=1

# パスを通す
# appディレクトリが作成される
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
