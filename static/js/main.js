// window.onload = () => {
//     let animation = new Animation({
//       "section.one .left, section.three .book, section.five .other": {
//         from: [
//           "left: -500px"
//         ],
//         to: [
//           "left: 0px"
//         ]
//       },
//       "section.one .right, section.three .complex, section.five .person": {
//         from: [
//           "right: -500px"
//         ],
//         to: [
//           "right: 0px"
//         ]
//       },
//       "section.two": {
//         from: [
//           "opacity: 0",
//           "transform: translateY(100px)"
//         ],
//         to: [
//           "opacity: 1",
//           "transform: translateY(0px)"
//         ]
//       },
//       ".grid10":{
//         parameters: [
//           "animation-duration: 0.8s",
//           "animation-fill-mode: forwards"
//         ],
//         to: [
//           "transform: translateY(-110px)",
//         ]
//       },
//       ".grid11": {
//         parameters: [
//           "animation-duration: 0.8s",
//           "animation-delay: 1s",
//           "animation-fill-mode: forwards"
//         ],
//         to: [
//           "transform: translateX(-150px)"
//         ]
//       }

//     });
//     animation.defaultParam(["animation-duration: .8s", "run: once", "animation-fill-mode: forwards","pixel-correction: -100px", "animation-time-function: ease-out"]);
//     animation.init();
//   };

//   if (window.history.replaceState){
//     window.history.replaceState(null, null, window.location.href);
//   };

// AjaxSender

// jQuery(function ($) {
//   $(document).ajaxSend(function () {
//       $("spinner-border").fadeIn(500);
//       var loading = `<div class="spinner-border text-warning"></div>&nbsp;&nbsp; Veuillez patienter...`
//       $("comment-sender").html(loading);
//   });

//   $("#comment-sender").click(function () {
//       $.ajax({
//           type: 'GET',
//           success: function (data) {
//               console.log(data);
//           }
//       }).done(function () {
//           setTimeout(function () {
//               $(".spinner-border").fadeOut(500);
//           }, 700);
//       });
//   });
// });


$.ajax({
    type: 'GET',
    url: '/vip-json/',
    success : function(response){
        console.log(response.data)
    },
    error : function (error) {
        console.log(error)
        const data = JSON.parse(response.data)
        console.log(data)
    }
})
