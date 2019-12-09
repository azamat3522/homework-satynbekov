$.ajax({

    url: 'http://localhost:8000/api/v1/login/',

    method: 'post',

    data: JSON.stringify({username: 'admin', password: 'admin'}),

    dataType: 'json',

    contentType: 'application/json',

    success: function(response, status){console.log(response);localStorage.setItem('apiToken', response.token);},

    error: function(response, status){console.log(response);}

});

$.ajax({

    url: 'http://localhost:8000/api/v1/logout/',

    method: 'post',

    headers: {"Authorization": 'Token ' + localStorage.getItem('apiToken')},

    dataType: 'json',

    success: function(response, status){console.log(response);},

    error: function(response, status){console.log(response);}

});



$.ajax({

    url: 'http://localhost:8000/api/v1/projects/',

    method: 'get',

    dataType: 'json',

    success: function (response, status) {
        console.log(response);
    },

    error: function (response, status) {
        console.log(response);
    }

});

$.ajax({

    url: 'http://localhost:8000/api/v1/tasks/',

    method: 'get',

    dataType: 'json',

    success: function(response, status){console.log(response);},

    error: function(response, status){console.log(response);}

});

$.ajax({

    url: 'http://localhost:8000/api/v1/tasks/',

    method: 'post',

    headers: {"Authorization": 'Token ' + localStorage.getItem('apiToken')},

    data: JSON.stringify({project: 3, summary: 'etst', description: 'tetst', status: 1, type: 1, assigned_to: 2,}),

    dataType: 'json',

    contentType: 'application/json',

    success: function(response, status){console.log(response);},

    error: function(response, status){console.log(response);}

});


$.ajax({

    url: 'http://localhost:8000/api/v1/tasks/16',

    method: 'delete',

    headers: {"Authorization": 'Token ' + localStorage.getItem('apiToken')},

    dataType: 'json',

    contentType: 'application/json',

    success: function(response, status){console.log('delete');},

    error: function(response, status){console.log(response);}
});




