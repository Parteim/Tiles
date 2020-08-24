
function imageMenu() {
    let profileImageMenu = document.getElementById('profile_image_menu');
    let openMenuBtn = document.getElementById('open_menu');
    let arrowBtn = document.getElementById('arrow_btn');
    let flag = false;

    let callUploadImgForm = document.getElementById('call_upload_img_form');

    openMenuBtn.addEventListener('click', function () {

        if (!flag) {
            profileImageMenu.style.transform = 'translate(-50%, 0%)';
            arrowBtn.style.transform = 'rotate(180deg)'
            setTimeout(function (){
                profileImageMenu.style.transform = 'translate(0%, 0%)';
            }, 600)
            flag = true;
        } else {
            profileImageMenu.style.transform = 'translate(-50%, 0)';
            arrowBtn.style.transform = 'rotate(0deg)'
            setTimeout(function () {
                profileImageMenu.style.transform = 'translate(-50%, -90%)';
            }, 600)
            flag = false;
        }
    });

    callUploadImgForm.addEventListener('click', function () {
       let uploadImgForm = document.createElement('form');
       uploadImgForm.className = 'upload_img_form';

       document.getElementsByTagName('body')[0].appendChild(uploadImgForm)
    });


}

imageMenu();

