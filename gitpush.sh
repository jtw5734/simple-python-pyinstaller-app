VERSION=${cat VERSION}
cd ~/web-service/api/simple-python-pyinstaller-app
git add .
git commit -m "ba$1"
git tag $VERSION
git push