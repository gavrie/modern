#!/bin/sh -x
export PYTHONPATH=$(PWD)
py.test $@
