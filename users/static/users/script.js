
$(document).on('click', '.addmore', function(){
    count = 0;
        var html = `<div class="mb-2">
                        <label class="block text-gray-700 text-sm font-bold mb-2" for="">Image </label>
                        <input type="file" name="images" accept="image/*" id="files" multiple onchange="previewMultiple(event)">
                    </div>
                    <div id = "preview" + count>`
        $('.postC').append(html)
        count +=1;
        console.log(count)
    // })
})

function previewMultiple(event){
    var images = document.getElementById("id_image");
    var number = images.files.length;
    capt = document.getElementById("c-text")
    for(i = 0; i < number; i++){
        var urls = URL.createObjectURL(event.target.files[i]);
        // document.getElementById("preview[i]").innerHTML += '<img src="'+urls+'">';
        // document.getElementById("preview").innerHTML += '<img src="'+urls+'">' + '<div class="">' + '<label class="block text-gray-700 text-sm font-bold mb-2" for="">Write a description </label>' + '<textarea name="caption" cols="40" rows="10" class="shadown appearance-none border rounded py-2 px-3 mr-10 vLargeTextField" id="id_caption"></textarea>' + '</div>';
        document.getElementById("preview").innerHTML += `<img src="${urls}" style="height:125px;"><div class="mb-2" id="c-text">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="">What's on your mind? </label>
        <div class="shadow appearance-none border rounded py-2 px-3 mr-10 text-grey-700">
            <textarea name="caption" cols="40" rows="10" class="vLargeTextField" id="id_caption"></textarea>
        </div>
    </div>`
        
    }
}

function showReply(id){
    var replyArea = document.getElementById(id);
    replyArea.classList.remove("hidden");
}
document.querySelectorAll('.more-button').forEach(button => {
    button.addEventListener('click', event => {
      // Find the parent .post element
      const post = event.target.parentNode;
      // Toggle the visibility of the .post-rest element
      post.querySelector('.post-rest').style.display = 'block';
      // Hide the "More" button
      event.target.style.display = 'none';
    });
  });

function toggleCommentForm(formId) {
    var formElement = document.getElementById(formId);
    if (formElement.style.display === "none") {
        formElement.style.display = "block";
    } else {
        formElement.style.display = "none";
}
}

$('.button-like').click(function(event) {
    window.location.reload()
});

document.getElementById("reply-form-{{ comment.id }}").onclick = function(event) {
    event.preventDefault();
    location.href = "#reply-form-{{ comment.id }}";
  };
// window.CSRF_TOKEN = "{{ csrf_token }}"
// $(document).on('click', '.button-like', function(){
//     console.log(this.id)
//     var post_id = this.id
//     $.ajax({
//         method:"POST",
//         url: '/posts/like',
//         data:{post_id:post_id, csrfmiddlewaretoken: window.CSRF_TOKEN}
//     })
//     window.location.reload()
// })

// $('.button-like').click(function(event) {
//     event.preventDefault();
//     var post_id = $(this).attr('id');
//     $.ajax({
//         url: '{% url "like" id=post.id %}',
//         type: 'POST',
//         data: {
//             'csrfmiddlewaretoken': '{{ csrf_token }}',
//             'post_id': post_id
//         },
//         success: function(data) {
//             // update the like button or display a message indicating that the post was liked
//         }
//     });
//     window.location.reload()
// });

// var timeleft = 3;
// var downloadTimer = setInterval(function(){
//   if(timeleft <= 0){
//     clearInterval(downloadTimer);
//     document.getElementById("countdown").innerHTML = ``;
//     window.location.href = "../../posts/feed";
    
//   } else{
//     document.getElementById("countdown").innerHTML = `Redirect you to daily feed in: <span class="text-warning"><strong>${timeleft}</strong></span>.`
//    }
//   timeleft -= 1;
// }, 1000);





