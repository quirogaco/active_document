export function manejo_tipo_archivo(tipo) {
    let tipo_documento = '';
    let tiposDoc = [
        'doc', 'docm', 'docx', 'dot', 'dotm', 'dotx', 'epub', 'fodt', 'htm', 'html', 'mht', 'odt', 'ott', 'pdf', 'rtf', 'txt', 'djvu', 'xps'
    ];
    let tiposCsv = [
        'csv', 'fods', 'ods', 'ots', 'xls', 'xlsm', 'xlsx', 'xlt', 'xltm', 'xltx'
    ];
    let tiposPpt = [
        'fodp', 'odp', 'otp', 'pot', 'potm', 'potx', 'pps', 'ppsm', 'ppsx', 'ppt', 'pptm', 'pptx'
    ];
    if (tiposDoc.includes(tipo)) {
        tipo_documento = 'text'
    }
    if (tiposCsv.includes(tipo)) {
        tipo_documento = 'spreadsheet'
    }
    if (tiposPpt.includes(tipo)) {
        tipo_documento = 'presentation'
    }
    return tipo_documento;
}