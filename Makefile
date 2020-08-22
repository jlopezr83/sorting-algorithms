DOCKER_IMAGE = sorting-algorithms

build:
	docker build -t ${DOCKER_IMAGE} .

test:
	docker run ${DOCKER_IMAGE} bash -c 'PYTHONPATH=./src pytest tests'

run:
	docker run ${DOCKER_IMAGE} bash -c 'PYTHONPATH=./src python src/main.py'

deploy: build test


.PHONY: build deploy test run
