// https://github.com/AleeeKoi/js-file-downloader

class DownloadException extends Error {
    constructor (message, request) {
        super(`Downloader error: ${message}`);
        this.request = request;
        this.name = 'DownloadException';
    }
};

const DEFAULT_PARAMS = {
    timeout: 1000000,
    headers: [],
    forceDesktopMode: false,
    autoStart: true,
    withCredentials: false,
    method: 'POST',
    data  : {},
    nameCallback: name => name
};

class JsFileDownloader {

    /**
     * Create a new JsFileDownloader instance
     * You need to define a {String} "url" params and other
     * @param {Object} customParams
     */
    constructor (customParams = {}) {
        this.params = Object.assign({}, DEFAULT_PARAMS, customParams);
        this.link = this.createLink();
        this.request = null;
        
        if (this.params.autoStart) return this.downloadFile();

        return this;
    }

    start () {
        return this.downloadFile();
    }

    downloadFile () {
        return new Promise((resolve, reject) => {
            this.initDonwload(resolve, reject);
        });
    }

    initDonwload (resolve, reject) {
        // fallback for old browsers
        if (!('download' in this.link) || this.isMobile()) {
            this.link.target = '_blank';
            this.link.href = this.params.url;
            this.clickLink();
            return resolve();
        }

        this.request = this.createRequest();

        if (!this.params.url) {
            return reject(new DownloadException('url param not defined!', this.request));
        }

        this.request.onload = () => {
            if (parseInt(this.request.status, 10) !== 200) {
                return reject(new DownloadException(`status code [${this.request.status}]`, this.request));
            }
            this.startDownload();
            return resolve(this);
        };

        this.request.ontimeout = () => {
            reject(new DownloadException('request timeout', this.request));
        };

        this.request.onerror = () => {
            reject(new DownloadException('network error', this.request));
        };

        var data = new FormData();
        for (const propiedad in this.params.data) {
            data.append(propiedad, this.params.data[propiedad])        
        }

        //data.append("datos", JSON.stringify(this.params.data))  
        //this.request.send(data);
        this.request.send(JSON.stringify(this.params.data));

        return this;
    }

    isMobile () {
        return !this.params.forceDesktopMode &&
        /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    }

    createRequest () {
        let request = new XMLHttpRequest();

        request.open(this.params.method, this.params.url, true);
        //request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        request.setRequestHeader('Content-type', 'application/json');
        this.params.headers.forEach(header => {
            request.setRequestHeader(header.name, header.value);
        });
        request.responseType = 'arraybuffer';
        if (this.params.process && typeof this.params.process === 'function') {
            request.addEventListener('progress', this.params.process);
        }
        request.timeout = this.params.timeout;
        request.withCredentials = !!this.params.withCredentials || !!this.params.includeCredentials;

        // JSON
        //request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        //xhr.setRequestHeader('Content-Type', 'application/json');

        return request;
    }

    getFileName () {
        // Forcing file name
        if (typeof this.params.filename === 'string') {
            return this.params.filename;
        }
        // Trying to get file name from response header
        let content = this.request.getResponseHeader('Content-Disposition');
        let contentParts = [];

        if (content) {
            contentParts = content.replace(/["']/g, '').match(/filename\*?=([^;]+)/);
        }

        const extractedName = contentParts && contentParts.length >= 1 ?
            contentParts[1] :
            this.params.url.split('/').pop().split('?')[0];

        return this.params.nameCallback(extractedName);
    }

    createLink () {
        let link = document.createElement('a');

        link.style.display = 'none';
        return link;
    }

    clickLink () {
        let event;
        try {
            event = new MouseEvent('click');
        } catch (e) {
            event = document.createEvent('MouseEvent');
            event.initMouseEvent('click', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        }

        this.link.dispatchEvent(event);
    }

    getFile (response, fileName) {
        let file = null;
        let options = { type: 'application/octet-stream' };

        try {
            file = new File([response], fileName, options);
        } catch (e) {
            file = new Blob([response], options);
            file.name = fileName;
            file.lastModifiedDate = new Date();
        }
        return file;
    }

    startDownload () {
        let fileName = this.getFileName();
        let file = this.getFile(this.request.response, fileName);

        // native IE
        if ('msSaveOrOpenBlob' in window.navigator) {
            return window.navigator.msSaveOrOpenBlob(file, fileName);
        }

        let objectUrl = window.URL.createObjectURL(file);

        this.link.href = objectUrl;
        this.link.download = fileName;
        this.clickLink();

        setTimeout(() => {
            (window.URL || window.webkitURL || window).revokeObjectURL(objectUrl);
        }, 1000 * 40);

        return this;
    }
}

export default JsFileDownloader;