#!/bin/bash
jekyll build
cp -fR ./_site/* ./docs
rm -r ./docs/docs/
git add .
git commit -m "new publish"
git push origin master
#git push --set-upstream origin unlam_deploy
#bibble pubs.bib publications.tmpl bibble mypapers.bib simple.html > mypapers.html