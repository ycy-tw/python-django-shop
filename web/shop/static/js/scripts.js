// image shop up immediately after selecting
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#image-preview').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$("#id_shop_img").change(function () {
    readURL(this)
});
$("#id_image").change(function () {
    readURL(this)
});
$("#id_profile_img").change(function () {
    readURL(this)
});