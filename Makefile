VERSION = $(shell cat setup.py | grep version | sed -e "s/version=//" -e "s/'//g" -e "s/,//" -e 's/^[ \t]*//')

install:
	python3 setup.py sdist
	@echo "Installing package using pip"
	python3-pip install --upgrade dist/trimfilename-$(VERSION).tar.gz

