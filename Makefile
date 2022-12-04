.PHONY: all site

all: latex site

latex/cv.tex: templates/cv.tex.j2 config.yaml
	python -m build latex

latex/cv.pdf:  latex/cv.tex
	make -C latex build

latex: latex/cv.pdf

site:
	pnpm build
