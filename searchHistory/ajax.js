
// type = "text/javascript" src = "{% static 'js/material.js' %}"
// type = "text/javascript"” src = "{% static 'js/jquery.min.js' %}"
// type = "text/javascript"
// $(document).on('submit', '#filter_form', function (e) {
//     e.preventDefault();
//     $.ajax({
//         type: 'POST',
//         url: '/user/create/',
//         data: {
//             u1: $('#u1').val(),
//             u2: $('#u2').val(),
//             u3: $('#u3').val(),
//             k1: $('#k1').val(),
//             k2: $('#k2').val(),
//             k3: $('#k3').val()
//       csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//         },
//         success: function () {
//             alert("Created New User!");
//         }
//     });
