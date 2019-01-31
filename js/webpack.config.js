const path = require('path');

module.exports = {
	entry: './index.js',
	output: {
		filename: 'injected_trex.js',
		path: path.resolve(__dirname, '../'),
	},
	mode: 'development',
}
