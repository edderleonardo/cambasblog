$(function() {
    let token = sessionStorage.getItem("token");

    if (token == null) {
        window.location.href = '/'
    } else {
        const div = $('#content-posts');
        const url = '/api/posts/';
        $.ajaxSetup({
          headers : {
            'Authorization' : 'Token ' + token
          }
        });

        $.getJSON(url, function (data) {
          for(let i in data.results) {
              div.append('<div class="col-lg-3 col-md-6 mb-4">\n' +
                  '        <div class="card h-100">\n' +
                  '          <img class="card-img-top" src="http://placehold.it/500x325" alt="">\n' +
                  '          <div class="card-body">\n' +
                  '            <h4 class="card-title">' + data.results[i].title + '</h4>\n' +
                  '            <p class="card-text">' + data.results[i].content.slice(0, 35) +  ' escrito por <b>' + data.results[i].author.email + ' </i></p> ' +
                  '          </div>\n' +
                  '          <div class="card-footer">\n' +
                  '            <a href="/post/detail/'+ data.results[i].pk +'" class="btn btn-primary"> Leer </a>\n' +
                  '          </div>\n' +
                  '        </div>\n' +
                  '      </div>')
          }
        });
    }
});