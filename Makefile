#.ONESHELL:
#.PHONY: install

venv: touchfile

touchfile: requirements.txt
	test -f env/pyvenv.cfg || python3 -m venv ./env
	. env/bin/activate; pip install -r requirements.txt
	touch touchfile

clean:
	find -iname "*.pyc" -delete
	find . -name '__pycache__' -exec rm '{}' \;


run: venv
	. env/bin/activate; python3 main.py

build: clean
	docker build -t queueoptimiser .

container: build
	docker-compose -f docker-compose.yml up

deep-clean:
	docker rm Queue_Optimiser
	docker image rm queueoptimiser

release:
	git add -u
	git commit -m "Release commit"
	git push dev
	git checkout main
	git merge dev
	git push main
	git checkout dev
