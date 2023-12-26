# nox configuration file
import nox

locations = "src", "tests", "noxfile.py", "docs/conf.py"
nox.options.sessions = "ruff", "mypy", "tests"


@nox.session(python=["3.12", "3.11", "3.10"])
def tests(session):
    """Run the test suite with pytest."""
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")


@nox.session(python=["3.12", "3.11", "3.10"])
def ruff(session):
    """Run the ruff linter."""
    args = session.posargs or locations
    session.install("ruff")
    session.run("ruff", *args)


@nox.session(python=["3.12", "3.11", "3.10"])
def mypy(session):
    """Type check using mypy."""
    args = session.posargs or locations
    session.install("mypy")
    session.run("mypy", *args)


@nox.session(python="3.12")
def docs(session) -> None:
    """Build the documentation."""
    session.install("sphinx")
    session.install("furo")
    session.run("sphinx-build", "docs", "docs/_build")
