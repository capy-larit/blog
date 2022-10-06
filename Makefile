#Makefile

.PHONY: format lint sec

format:
	@isort .
	@blue .
lint:
	@blue . --check
	@isort . --check
	@prospector --with-tool pydocstyle --doc-warning
sec:
	@pip-audit