start:
	docker-compose up --build -d
stop:
	docker-compose stop

restart: stop start

logs:
	docker-compose logs --tail 100

logs:
	docker-compose logs --tail 100