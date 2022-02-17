BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output/gen
CONFFILE=$(BASEDIR)/config.toml
# ln -s $CACHE output 

BASE_URL = https://biluohc.github.io
GITHUB_REPO = git@github.com:biluohc/biluohc.github.io.git
GITHUB_PAGES_BRANCH=pages

DATE=$(shell TZ=Hongkong date '+%Y-%m%d-%H%M')
MSG=$(shell git describe --always --abbrev=6 --dirty=_)

DEBUG ?= 0
ifeq ($(DEBUG), 1)
endif

help h:
	@echo 'Makefile for the Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make new/n                            generate a new post          	  '
	@echo '   make build/b                          (re)generate the web site          '
	@echo '   make clean/c                          remove the generated files         '
	@echo '   make publish/p                        generate using production settings '
	@echo '   make serve/s              		    serve site at http://127.0.0.1:1111'
	@echo '   make github/g                         deploy the web site via github pages'
	@echo '                                                                           '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 build   '
	@echo '                                                                           '

clean c:
	cd $(OUTPUTDIR) && rm -rf *

build b:
	zola build

serve s:
	zola serve -o $(OUTPUTDIR)

f:b
	fht2p -p 1111 -rv $(OUTPUTDIR)

publish p:
	zola build --base-url $(BASE_URL)

githubinit: publish
	cd $(OUTPUTDIR) && \
	git init && git checkout -b $(GITHUB_PAGES_BRANCH) && \
	git add . && git commit -a -m $(DATE)-$(MSG) && \
	git remote add origin $(GITHUB_REPO) && \
	git push origin $(GITHUB_PAGES_BRANCH) -f 

github g: publish
	cd $(OUTPUTDIR) && \
	git clone --no-checkout --branch $(GITHUB_PAGES_BRANCH) $(GITHUB_REPO) && \
	git add . && git commit -a -m $(DATE)-$(MSG) && \
	git remote add origin $(GITHUB_REPO) && \
	git push origin $(GITHUB_PAGES_BRANCH)

new n:
	cp -rp content/pages/post_sample  content/posts/$(DATE)_
