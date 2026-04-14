set shell := ["zsh", "-cu"]

default:
    just all

all: latex site

latex-source:
    UV_CACHE_DIR=.uv-cache uv run python build.py latex

latex-pdf: latex-source
    just --justfile latex/Justfile build

latex: latex-pdf

site:
    pnpm build
