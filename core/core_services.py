from tenants.models import Tenant


def host_from_request(request):
    # get name from request
    host_name = request.get_host()
    prefix_domain = host_name.split('.')[0]
    tenant = Tenant.objects.filter(domain_prefix=prefix_domain).first()
    return tenant


def get_tenants_map():
    return {
        "renan.tasks.localhost": "renan",
        "steve.tasks.localhost": "steve",
    }


