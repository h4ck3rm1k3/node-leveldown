
build2 :
	/usr/local/lib/node_modules/npm/bin/node-gyp-bin/node-gyp build --nodedir=~/experiments/node-stuff/node --debug

configure :
	/usr/local/lib/node_modules/npm/bin/node-gyp-bin/node-gyp configure --nodedir=~/experiments/node-stuff/node --debug

npm:
	npm install --nodedir=~/experiments/node-stuff/node
