#!/bin/bash
git add .
echo -n "Please Enter Your Push Record ->"
read record
git status
git commit -m $record
git push origin master

echo "done"