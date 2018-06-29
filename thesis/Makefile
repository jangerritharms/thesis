# LaTeX Makefile
FILE=report
FILE_CHAPTER=report_chapter

all: $(FILE).pdf

.PHONY: clean

clean:
	rm -rf *.blg 
	rm -rf *.out 
	rm -rf *.bbl 
	rm -rf *.log
	rm -rf *.ind
	rm -rf *.ilg
	rm -rf *.lot
	rm -rf *.lof
	rm -rf *.ind
	rm -rf *.idx
	rm -rf *.aux
	rm -rf *.toc
	rm -f ${FILE}.pdf


$(FILE_CHAPTER).pdf: report_chapter.tex *.bib *.sty
	xelatex -shell-escape $(FILE_CHAPTER).tex
	xelatex -shell-escape $(FILE_CHAPTER).tex
	bibtex $(FILE_CHAPTER).aux
	xelatex -shell-escape $(FILE_CHAPTER).tex
	xelatex -shell-escape $(FILE_CHAPTER).tex

$(FILE).pdf: *.tex *.bib *.sty
	xelatex -shell-escape $(FILE).tex
	xelatex -shell-escape $(FILE).tex
	bibtex $(FILE).aux
	xelatex -shell-escape $(FILE).tex
	xelatex -shell-escape $(FILE).tex