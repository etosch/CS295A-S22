SHELL:=/bin/bash
PYTHON=$(shell [ -z "`which python3`" ] && echo "python" || echo "python3")
PIP=$(shell [ -z "`which pip3`" ] && echo "pip" || echo "pip3")
.PHONY: build deploy

venv:
	$(PYTHON) -m venv venv && $(PIP) install -r REQUIREMENTS.txt 

build: venv
	( \
		source venv/bin/activate; \
		git pull; \
		pip install -r REQUIREMENTS.txt; \
		mkdocs build; \
		xmlmerge site/feed_rss_created.xml site/feed_rss_updated.xml > site/feed_rss.xml; \
	)
	

deploy: build
	(\
		source venv/bin/activate; \
		mkdocs gh-deploy; \
		cp -r site/* ../CS295A-S22/; \
		git add site; \
		git commit -m 'auto-committing from Makefile'; \
		git push origin main; \
	)
