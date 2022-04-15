SHELL:=/bin/bash
PYTHON=$(shell [ -z "`which python3`" ] && echo "python" || echo "python3")
.PHONY: build deploy clean

venv:
	$(PYTHON) -m venv venv && source venv/bin/activate && pip install -r REQUIREMENTS.txt 

build: venv
	( \
		source venv/bin/activate; \
		git pull; \
		pip install -r REQUIREMENTS.txt; \
		mkdocs build; \
	)
	

deploy: build
	(\
		source venv/bin/activate; \
		mkdocs build; \
		mkdocs gh-deploy; \
		cp -r site/* ../CS295A-S22/; \
		git add site; \
		git commit -m 'auto-committing from Makefile'; \
		git push origin main; \
	)

clean: 
	(\
		rm *.html; \
		rm *.xml; \
		rm -rf lectures blog assignments code; \
		rm sitemap.xml.gz; \
	)
