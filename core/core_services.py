def host_from_request(request):
    # get name from request
    host_name = request.get_host()
    prefix_domain = host_name.split('.')[0]
    return prefix_domain