$(function() {
    const content_posts = $('#content-posts');
    const author = $('#select-author');
    const country = $('#select-country');
    const btn_filter = $('#btn-filter');

    const url_countries = '/api/countries/';
    const url_authors = '/api/authors/';

    $.getJSON(url_countries, function (data) {
      country.append("<option value disabled selected> País </option>");
      for(let i in data.results) {
        country.append("<option value=" + data.results[i].id + ">" + data.results[i].name + "</option>");
      }
    });

    $.getJSON(url_authors, function (data) {
      author.append("<option value disabled selected> Autor </option>");
      for(let i in data.results) {
        author.append("<option value=" + data.results[i].id + ">" + data.results[i].email + "</option>");
      }
    });

    function get_data(url) {
        $.getJSON(url, function (data) {

            content_posts.empty();
            content_posts.removeClass('posts');
            if (data.count > 0 ) {
                for(let i in data.results) {
                    content_posts.append('<div class="col-lg-3 col-md-6 mb-4">\n' +
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
            } else {
                content_posts.addClass('posts');
                content_posts.append("<h1>No existen post para esta búsqueda. 😞</h1>")
            }
        })
    }

    btn_filter.click(function () {
        let author_id= author.val();
        let country_id = country.val();
        let url_filter;
        if (author_id == null) {
            url_filter = '/api/posts/?author=&author__country=' + country_id;
            get_data(url_filter);
        }
        if (country_id == null) {
            url_filter = '/api/posts/?author='+ author_id +'&author__country=';
            get_data(url_filter);
        }
        if (author_id != null && country_id != null) {
            url_filter = '/api/posts/?author='+ author_id +'&author__country=' + country_id;
            get_data(url_filter);
        }
    })

});