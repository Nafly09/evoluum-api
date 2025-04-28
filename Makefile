CONTAINER_NAME=evoluum_api

up:
	sudo docker compose up

down:
	sudo docker compose down

update-migration:
	sudo docker compose exec $(CONTAINER_NAME) alembic upgrade head