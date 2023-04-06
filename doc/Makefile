TARGETS = \
	Aslak\ Johansen\ Research\ -\ Poster.pdf \



all: ${TARGETS}

clean:
	touch ${TARGETS}
	rm -f ${TARGETS}

mrproper: clean
	touch d.aux d.log d~ d.nav d.out d.snm d.toc includes.d
	rm -f *.aux *.log *~ *.nav *.out *.snm *.toc includes.*



.includes:
	rm -Rf .includes
	mkdir .includes

.includes/poster.timestamp: .includes poster.tex figs/*.svg
	python3 ../bin/process-pollpoll.py
	python3 ../bin/process-pushpush.py
	python3 ../bin/process-metadata.py
	cd .. ; bin/generate-tex-includes PDF doc/poster.tex doc
	touch .includes/poster.timestamp



Aslak\ Johansen\ Research\ -\ Poster.pdf: poster.tex .includes/poster.timestamp
	pdflatex -shell-escape poster.tex
	pdflatex -shell-escape poster.tex
	mv poster.pdf Aslak\ Johansen\ Research\ -\ Poster.pdf

