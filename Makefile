init:
	echo "init repository ..."
	git init
	sleep 1
	git add .
	sleep 1
	git commit -m "Commit #(0000)"
	sleep 1
	git branch -M main
	sleep 1
	git remote add origin https://github.com/EDJINEDJA/PilotD.git
	sleep 1
	git push -u origin main
push:
	git add .
	git commit -m $(var)
	git push -u origin main
env:
	pipenv install

enable_env:
	pipenv shell
freeze:
	pipenv requirements > requirements.txt
setup:
	python setup.py --config ./config/config.yaml
run:
	uvicorn index:app --reload
