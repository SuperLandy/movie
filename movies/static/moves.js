// csrf_token
jQuery(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            const cookies = document.cookie.split(';');
            for (const i = 0; i < cookies.length; i++) {
                const cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        const host = document.location.host; // host + port
        const protocol = document.location.protocol;
        const sr_origin = '//' + host;
        const origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
})


// user login
$(function () {
     $('#btn_login').click(function () {
         const username = $("#username").val();
         const password = $("#password").val();
         $.post({
            url: '/accounts/login/',
            data: {'username': username, 'password': password},
            success: function (result) {
                if (result.code === '0000'){window.location.href="/movies/"}
                else {alert(result.msg)}
            }})
     })
})


// movie search
$(function () {
     $('#btn_search').click(function () {
         const passageway = $("#passageway").val();
         const movie_url = $("#movie_url").val();
         $.post({
            url: '/movies/',
            data: {'passageway': passageway, 'movie_url': movie_url},
            success: function (data) {
                if (data.code === '0000'){window.location.href=data.result}
                else {alert(data.result)}
            }})
     })
})

