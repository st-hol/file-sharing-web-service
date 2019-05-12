// $(function () {
//     $('#upload-ajax').click(function () {
//         var form_data = new FormData($('#file-upload-ajax-form')[0]);
//         $.ajax({
//             type: 'POST',
//             url: '/upload',
//             dataType: 'json',
//             data: form_data,
//             contentType: false,
//             cache: false,
//             processData: false,
//             success: function () {
//                 console.log('success');
//                 location.replace('https://developer.mozilla.org/en-US/docs/Web/API/Location.reload');
//                 // alert("file id was uploaded");
//                 // alert(data);
//                 // location.reload();
//             },
//             error: function (data) {
//                 console.log('Error:', data);
//             },
//         });
//     });
// });

// $(function() {
//     $('#upload-ajax').click(function() {
//         var form_data = new FormData($('#file-upload-ajax-form')[0]);
//         $.ajax({
//             type: 'POST',
//             url: '/upload/',
//             data: form_data,
//             contentType: false,
//             cache: false,
//             processData: false,
//             success: function(data) {
//                 console.log('Success!');
//                     // location.reload();
//                     // alert('fsda');
//             },
//         });
//     });
// });

$(document).ready(function () {
    $('#file-upload-ajax-form').submit(function (event) {
        var form_data = new FormData($('#file-upload-ajax-form')[0]);
        $.ajax({
            data: form_data,
            type: 'POST',
            url: '/upload'
        })
            .done(function (data) {

                if (data.error) {
                    $('#errorAlert').text(data.error).show();
                    $('#successAlert').hide();
                }
                else {
                    $('#successAlert').text(data.name).show();
                    $('#errorAlert').hide();
                }

            });

        event.preventDefault();

    });

});
