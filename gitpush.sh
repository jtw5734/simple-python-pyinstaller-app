VERSION=$(cat VERSION)
echo $VERSION
cd ~/web-service/api/simple-python-pyinstaller-app
git add .
git commit -m "ba"
git tag "$VERSION"
git push