const Fs = require('fs')
const Axios = require('axios')
const readerFile = require('./reader-file').readerFile;

const catalog = readerFile('./docs/catalog.xlsx')

async function download(url, filename) {
    const writer = Fs.createWriteStream(filename)

    const response = await Axios({
        url,
        method: 'GET',
        responseType: 'stream'
    })

    response.data.pipe(writer)

    return new Promise((resolve, reject) => {
        writer.on('finish', resolve)
        writer.on('error', reject)
    })
}

const imagesDownload = function () {
    catalog.data.map(function (model) {
        const imageName = model.Codigo.toUpperCase();
        const uriImage = `https://eos-web-content.s3.amazonaws.com/images/catalogo/${imageName}/0_large.jpg`
        const filename = `img_original/`.concat(`${imageName}.jpg`);
        download(uriImage, filename).then(() => {
            console.log(`Download successful: ${imageName}`);
        }).catch(e => {
            console.log(e);
        });
    });
}

imagesDownload();

