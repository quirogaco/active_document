// Office
let doc   = "application/msword";
let docx  = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"; 
let xls   = "application/vnd.ms-excel";
let xlsx  = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet";

// Imagenes
let gif   = "image/gif";
let png   = "image/png";
let bmp   = "image/bmp";

// Video. Audio
let avi   = "video/x-msvideo";
let mp3   = "audio/mpeg";

// Otros
let pdf   = "application/pdf";
let zip   = "application/zip";

let mimes = {
    doc : doc,
    docx: docx,
    xls : xls,
    xlsx: xlsx,    
    gif : gif,
    png : png,
    bmp : bmp,
    avi : avi,
    mp3 : mp3,
    pdf : pdf,
    zip : zip,
}


const crea_mime = function(lista=[]) {
    let lista_mimes = [];
    let mime;
    for (let elemento of lista) {
        mime = mimes[elemento];
        if (mime != undefined) {
            lista_mimes.push(mime)
        }
    }

    return lista_mimes.join(", ")
}

export default { 
    crea_mime: crea_mime,
    mimes    : mimes
}