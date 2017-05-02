# These targets are not files
.PHONY: test lint todo

clean:
	# Remove files not in source control
	find . -type f -name "*.pyc" -delete

todo:
	# Look for areas of the code that need updating when some event has taken place
	grep -rnH TODO

test:
	pytest

lint:
	flake8 .

## Install / Upgrade
install:
	pip install -r requirements.txt

upgrade:
	pip install --upgrade -r requirements.txt


## Deployment
deploy_production:
	git push --tag origin master
	git push heroku master

migrate_production:
	heroku run python manage.py migrate --remote heroku

collectstatic_production:
	./manage.py collectstatic --noinput

# shortcuts for deploy to the production
dp: deploy_production
dmp: deploy_production migrate_production
cp: collectstatic_production
