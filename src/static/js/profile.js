

function imageMenu() {

    let callUploadImgForm = document.getElementById('call_upload_img_form');
    let uploadImgForm = document.createElement('form');
    let imageField = document.createElement('input');
    let imagedLabel = document.createElement('label');
    let closeBtnUploadImageForm = document.createElement('button');
    let sendRequestBtn = document.createElement('button');

    uploadImgForm.className = 'upload_img_form';
    uploadImgForm.appendChild(imagedLabel);
    uploadImgForm.appendChild(closeBtnUploadImageForm);
    uploadImgForm.appendChild(sendRequestBtn);
    imageField.accept = 'image/*';
    imageField.name = 'image';
    imageField.type = 'file';
    imageField.className = 'upload_image_field';
    imagedLabel.draggable = true;
    imagedLabel.className = 'upload_image_label';
    imagedLabel.innerHTML = '<i class="fas fa-file-upload"></i>';
    imagedLabel.appendChild(imageField);
    closeBtnUploadImageForm.className = 'close_upload_image_form_bnt';
    closeBtnUploadImageForm.type = 'button';
    closeBtnUploadImageForm.innerHTML = '<i class="fas fa-times"></i>';
    sendRequestBtn.type = 'submit';
    sendRequestBtn.className = 'send_request_btn';
    sendRequestBtn.innerHTML = 'Send <i class="fas fa-chevron-right"></i>';

    callUploadImgForm.addEventListener('click', function () {
        document.getElementsByTagName('body')[0].appendChild(uploadImgForm);

        setTimeout(function () {
            uploadImgForm.style.height = ' 20%';
            uploadImgForm.style.opacity = '1';
        }, 400)

    });

    uploadImgForm.addEventListener('submit', function (event) {
        event.preventDefault();
    });

    closeBtnUploadImageForm.addEventListener('click', function () {
        uploadImgForm.style.height = '0';
        uploadImgForm.style.opacity = '0';

        setTimeout(function () {
            document.getElementsByTagName('body')[0].removeChild(uploadImgForm);
        },500)

    });


}

imageMenu();

