# Makefile for Zoom plugin plugin 

default: deploy

deploy: .
	cd env/Scripts && ./tensorboard.exe --logdir=../../logs --host=127.0.0.1
