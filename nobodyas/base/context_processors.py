def navbar(request):
    current_url = request.path_info

    navbar_list = [
        {
            'name': 'Home',
            'url_name': 'home',
            'active': '/' == current_url
        },
        {
            'name': 'Posts',
            'url_name': 'posts',
            'active': '/posts/' == current_url
        },
        {
            'name': 'Portfolio',
            'url_name': 'portfolio',
            'active': '/portfolio/' == current_url
        },
    ]

    return {'navbar_list': navbar_list}
