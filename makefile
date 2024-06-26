start:
	docker-compose up --build -d
stop:
	docker-compose stop

restart: stop start