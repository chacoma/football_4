#!/bin/bash

#git init

git add .

#excluyo la que no quiero
#git reset -- path/to/folder/*

git commit -m "commit "

git branch -M main

#git remote add origin git@github.com:chacoma/football_4.git

git push -u origin main
