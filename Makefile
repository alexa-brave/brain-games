install:
	uv sync

mind-games:
	uv run maind-games

build:
	uv-build


package-install:
	uv tool install dist/*.whl
