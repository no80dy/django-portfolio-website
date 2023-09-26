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
            'name': 'Profile',
            'url_name': 'profile',
            'active': '/profile/' == current_url
        },
    ]

    return {'navbar_list': navbar_list}
