include docker/.env
pf := $(COMPOSE_FILE)
pn := $(PROJECT_NAME)

help: ## ヘルプを表示
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## 開発環境構築(ビルド)
	make destroy
	docker compose -f $(pf) -p $(pn) build --no-cache
	docker compose -f $(pf) -p $(pn) down --volumes
	docker compose -f $(pf) -p $(pn) up -d
	./docker/wait-for-db.sh
	docker compose -f $(pf) -p $(pn) exec -T db mysql -psecret < docker/setup.dev.sql
	make reinstall
	docker compose -f $(pf) -p $(pn) exec -it fastapi pipenv run alembic upgrade head
	make reset

reinstall: ## リインストール
	rm -rf apps/user-api/.venev
	docker compose -f $(pf) -p $(pn) exec -it fastapi pipenv install --dev


init: ## 開発環境構築
	cp apps/user-api/.env.example apps/user-api/.env
	make build

up: ## 開発環境up
	docker compose -f $(pf) -p $(pn) up -d

down: ## 開発環境down
	docker compose -f $(pf) -p $(pn) down

destroy: ## 開発環境削除
	make down
	docker network ls -qf name=$(pn) | xargs docker network rm
	docker container ls -a -qf name=$(pn) | xargs docker container rm
	docker volume ls -qf name=$(pn) | xargs docker volume rm

reset:
	make sqlalchemy-reset

reset:
# dbのマイグレーションをリセットして良い場合のみ実行
# マイグレーションをリセットしない場合は、コマンドを変更すること
# 運用を始めたらコマンドを変更すること
	rm -rf common/migrations/versions/*
	docker compose -f $(pf) -p $(pn) exec -it fastapi pipenv run python app/console/commands/drop_all_tables.py
	docker compose -f $(pf) -p $(pn) exec -it fastapi pipenv run alembic revision --autogenerate -m 'comment'
	docker compose -f $(pf) -p $(pn) exec -it fastapi pipenv run alembic upgrade head
	docker compose -f $(pf) -p $(pn) exec -it fastapi pipenv run python app/console/commands/seeds.py

user-api-shell: ## shellに入る
	docker compose -f $(pf) -p $(pn) exec -it fastapi bash

db-shell: ## shellに入る
	docker compose -f $(pf) -p $(pn) exec -it db bash

check: ## コードフォーマット
	docker compose -f $(pf) -p $(pn) exec -it fastapi pipenv run isort .
	docker compose -f $(pf) -p $(pn) exec -it fastapi pipenv run black .
	docker compose -f $(pf) -p $(pn) exec -it fastapi pipenv run flake8 .
	docker compose -f $(pf) -p $(pn) exec -it fastapi pipenv run mypy .

user-api-run: ## サーバー起動
	docker compose -f $(pf) -p $(pn) exec -it fastapi pipenv run uvicorn main:app --host 0.0.0.0 --reload --port 8000


push: ## push
# make format
	git switch main
	git pull origin main
	git add .
	git commit -m "Commit at $$(date +'%Y-%m-%d %H:%M:%S')"
	git push origin main

cc: ## キャッシュ クリア
	rm -rf apps/user-api/log/fastapi.log
	rm -rf apps/user-api/log/sqlalchemy.log
	rm -rf apps/user-api/.mypy_cache
