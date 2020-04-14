#!/bin/bash
jekyll build
cp -fR ./_site/* ./docs
rm -r ./docs/docs/
git add .
git commit -m "new publish"
git push origin master