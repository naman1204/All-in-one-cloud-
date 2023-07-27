document.getElementById('upload-button').addEventListener('click', function() {
    var file = document.getElementById('file-upload').files[0];
    var formData = new FormData();
    formData.append('file', file);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://saas.upload.s3-website.ap-south-1.amazonaws.com/');
    xhr.onload = function () {
        if (xhr.status === 200) {
            console.log(this.responseText);
        } else {
            console.error('File upload failed');
        }
    };
    xhr.send(formData);
});

document.getElementById('download-button').addEventListener('click', function() {
    var filename = document.getElementById('file-download').value;

    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/download?filename=' + filename, true);
    xhr.responseType = 'blob';
    xhr.onload = function () {
        if (xhr.status === 200) {
            var blob = new Blob([xhr.response], {type: 'application/octet-stream'});
            var url = window.URL.createObjectURL(blob);
            var a = document.createElement('a');
            a.href = url;
            a.download = filename;
            a.click();
        } else {
            console.error('File download failed');
        }
    };
    xhr.send();
});

