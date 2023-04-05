const manejoTipoDocumento = function (tipoArchivo) {
    let docType = '';
    let tipoArchivosDoc = [
        'doc', 'docm', 'docx', 'dot', 'dotm', 'dotx', 'epub', 'fodt', 'htm', 'html', 'mht', 'odt', 'ott', 'pdf', 'rtf', 'txt', 'djvu', 'xps'
    ];
    let tipoArchivosCsv = [
        'csv', 'fods', 'ods', 'ots', 'xls', 'xlsm', 'xlsx', 'xlt', 'xltm', 'xltx'
    ];
    let tipoArchivosPPt = [
        'fodp', 'odp', 'otp', 'pot', 'potm', 'potx', 'pps', 'ppsm', 'ppsx', 'ppt', 'pptm', 'pptx'
    ];
    if (tipoArchivosDoc.includes(tipoArchivo)) {
        docType = 'text'
    }
    if (tipoArchivosCsv.includes(tipoArchivo)) {
        docType = 'spreadsheet'
    }
    if (tipoArchivosPPt.includes(tipoArchivo)) {
        docType = 'presentation'
    }
    return docType;
}

export default {
    manejoTipoDocumento: manejoTipoDocumento
}