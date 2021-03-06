#!/bin/sh
set -e

echo "Starting build on executor $EXECUTOR_NUMBER..."

cd $WORKSPACE
VENV=$WORKSPACE/venv
ES_HOST='http://jenkins-es20:9200'

# Make sure there's no old pyc files around.
find . -name '*.pyc' -exec rm {} \;

# Handle virtualenv creation.
if [ ! -d "$VENV/bin" ]; then
  echo "No virtualenv found.  Making one..."
  virtualenv $VENV --system-site-packages
fi
source $VENV/bin/activate

echo "Running tests"

make build
export ES_HOST=$ES_HOST && make test

echo "Calculating coverage..."

bin/coverage xml $(find monolith/client -name '*.py')

echo "FIN"
