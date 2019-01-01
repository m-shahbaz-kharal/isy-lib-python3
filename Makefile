
PEP8=pep8
#PEP8ARG=--ignore=E127,E265,E101,E128,E201,E202,E203,E211,E302,E303,W191,E501
# E203 space before ":"
# E201 whitespace after '('
# E202 whitespace before ')'
PEP8ARG=--ignore=E203,E201,E202
REPO=git@github.com:evilpete/ISYlib-python.git
PROGS=
PLIB=./ISY.py
GIT=git

all:
	echo "Be more exact"

t: style

FILES= ISY/IsyClass.py ISY/IsyExceptionClass.py ISY/IsyNodeClass.py ISY/IsyProgramClass.py ISY/IsyUtilClass.py ISY/IsyVarClass.py ISY/IsyDiscover.py ISY/IsyEventData.py ISY/IsyEvent.py ISY/_isyclimate.py ISY/_isynode.py ISY/_isyvar.py ISY/_isynet_resources.py ISY/__init__.py ISY/_isy_printevent.py

BINFILES= bin/isy_find.py bin/isy_nodes.py bin/isy_log.py  bin/isy_progs.py bin/isy_showevents.py bin/isy_var.py bin/isy_nestset.py bin/isy_net_wol.py bin/isy_net_res.py bin/isy_web.py

#README.txt:  ${FILES}
#	pydoc ISY > README.txt
#	git commit --message "file GENERATED by pydoc" README.txt

syntax:
	for targ in ${FILES} ; do \
	    python $$targ ; \
	done 
	for targ in ${BINFILES} ; do \
	    echo $$targ ; \
	    python -m py_compile $$targ ; \
	done 

style:
	${PEP8} ${PEP8ARG} ${FILES}


list: ${FILES}
	for targ in ${FILES} ; do  \
	    echo $$targ ; \
	    egrep -h '^ *class |^ *def |^    ##|^def ' $$targ ;\
	done

doc: 
	pydoc ${FILES}


lint: 
	pylint -d W0312,C0111,C0301,C0103 ${FILES}  

clean:
	rm bin/*.pyc ISY/*.pyc

checkin: commit push

commit: README.txt
	${GIT} commit -a

diff:
	${GIT} diff

status:
	${GIT} status

push:
	${GIT} push

pull:
	${GIT} pull

setup: setup.py README.txt
	python setup.py sdist
	git commit --message "file GENERATED by distutils" MANIFEST 

${PLBS}:
	@echo ${GIT} pull