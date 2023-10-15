up-production:
	docker compose -f docker-compose-prod.yml up

down-production:
	docker compose -f docker-compose-prod.yml down

up-develop:
	docker compose -f docker-compose.yml up

down-develop:
	docker compose -f docker-compose.yml down

