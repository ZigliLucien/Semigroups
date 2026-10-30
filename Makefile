LATEXMK ?= latexmk
.PHONY: all clean
all:
	$(LATEXMK) -pdfps main.tex
clean:
	$(LATEXMK) -c main.tex
