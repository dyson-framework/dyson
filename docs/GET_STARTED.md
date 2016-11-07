Get Started with Dyson
======================

## Run tests within a package
dyson-test tests/general

## Run a suite of tests
dyson-suite suite.yml

## Run a suite of tests by tags
dyson-suite suite.yml -t login

## Run a login test overriding the username
dyson-test tests/general -e "username=testusername password=testpassword"

## Run a suite in production environment and dev
dyson-suite suite.yml -d dev.yml
dyson-suite suite.yml -d prod.yml

## Run a test in production environment
dyson-test tests/
