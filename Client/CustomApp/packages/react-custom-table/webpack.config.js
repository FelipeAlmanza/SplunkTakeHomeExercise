const path = require('path');
const { merge: webpackMerge } = require('webpack-merge');
const baseComponentConfig = require('@splunk/webpack-configs/component.config').default;

module.exports = webpackMerge(baseComponentConfig, {
    entry: {
        ReactCustomTable: path.join(__dirname, 'src/ReactCustomTable.jsx'),
    },
    output: {
        path: path.join(__dirname),
    },
    resolve: {
        fallback: { querystring: require.resolve('querystring-es3') },
    },
});
