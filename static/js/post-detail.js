$(function() {

    let token = sessionStorage.getItem("token");
    if (token == null) {
        window.location.href = '/'
    } else {

         let url_pk = window.location.href.split('/');
         let pk = url_pk[5]

         let title_post = $('#title-post');
         let date = $('#date-post');
         let autor = $('#author-post');
         let country = $('#author-country');
         let content = $('#content-post');

         $.ajaxSetup({
             headers : {
                'Authorization' : 'Token ' + token
             }
         });
         const url = '/api/posts/' + pk + '/';

         $.getJSON(url, function (data) {

                title_post.append("<h1>" + data.title + "</h1>");
                date.append("<span>"+ moment(data.published).format('MMMM Do YYYY, h:mm:ss a') +"</span>")
                if (data.author.name) {
                    autor.append("<span> <b>Autor:</b> " + data.author.name + ' ' + data.author.last_name + "</span>");
                } else {
                    autor.append("<span> <b>Autor:</b> " + data.author.email + "</span>");
                }
                country.append("<span> <b>País: </b>" + data.author.country.name + "</span>");
                content.append("<p>" + data.content + "</p>")
         })

    }
});