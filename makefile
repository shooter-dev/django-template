VENV_NAME?=venv
PYTHON=${VENV_NAME}/bin/python


freeze:
	${PYTHON} -m pip freeze > requirements.txt


run:
	${PYTHON} ./src/manage.py runserver


tests:
	#make fixtures env=test
	${PYTHON} -m pytest --cov=./src/ --cov-report=html -s


database:
	rm -f ./src/*/migrations/[0-9]*
	rm -f ./src/core/database.db

	${PYTHON} ./src/manage.py flush
	${PYTHON} ./src/manage.py makemigrations
	${PYTHON} ./src/manage.py migrate
	#./src/manage.py shell -c "from libs.create_user import create_users;


fix:
	${PYTHON} -m black --line-length 120 ./src
	${PYTHON} -m autopep8 --recursive --in-place --aggressive --max-line-length=120 ./src/*


analyse:
	${PYTHON} -m flake8 --max-line-length=120 ./src
	${PYTHON} -m pylint ./src
	${PYTHON} -m pycodestyle --max-line-length=120 ./src


code:
	make fix
	make analyse


clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf htmlcov
