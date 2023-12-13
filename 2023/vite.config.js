const { resolve } = require('path')
module.exports = {
    build: {
        rollupOptions: {
            input: [
                resolve(__dirname, 'index.html'),
                resolve(__dirname, '01.html'),
                resolve(__dirname, '02.html'),
                resolve(__dirname, '03.html'),
                resolve(__dirname, '04.html'),
                resolve(__dirname, '05.html'),
                resolve(__dirname, '06.html'),
                resolve(__dirname, '07.html'),
                resolve(__dirname, '08.html'),
            ],
        },
    },
}
