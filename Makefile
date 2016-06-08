update-py:
	virtualenv --no-site-packages venv

install-deps:
	pip install -r requirements.txt

update-deps:
	pip install -U `pip list --local | cut -d ' ' -f 1`
