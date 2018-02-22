import json
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.shortcuts import render
from app import models


def host(request):
    """
    host函数通过request区别get和post方法，如果是request是get方法,就从数据库中查询数据，然后将查询的数据返回给HTML进行渲染展示
    如果是request是post方法,就从request中提取数据，然后进行数据库添加操作
    :param request:
    :return:
    """
    if request.method == "GET":
        v1 = models.Host.objects.filter(nid__gt=0)
        b_list = models.Business.objects.all()
        return render(request, 'host.html', {'v1': v1, "b_list": b_list})

    elif request.method == "POST":

        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        models.Host.objects.create(hostname=h,
                                   ip=i,
                                   port=p,
                                   b_id=b,
                                   )
        return redirect('/app/host')


def host_detail(request):
    """
    :param request:
    :return:
    """
    if request.method == "GET":
        nid = request.GET.get('nid')
        aid = request.GET.get('aid')
        v1 = models.Host.objects.filter(nid=nid)
        v2 = models.Application.objects.filter(id=aid)
        return render(request, 'host_detail.html', {'v1': v1, "v2": v2})


# 通过ajax方式提交数据,服务端提取数据操作后返回的示例：
def test_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        models.Host.objects.create(hostname=h,
                                   ip=i,
                                   port=p,
                                   b_id=b)
    except Exception as e:
        ret['status'] = False
        ret['error'] = "request error"
    return HttpResponse(json.dumps(ret))


# 编辑操作
def edit(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        nid = request.POST.get('nid')
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        models.Host.objects.filter(nid=nid).update(
            hostname=h,
            ip=i,
            port=p,
            b_id=b
        )
    except Exception as e:
            ret['status'] = False
            ret['error'] = "hostname error"
    return HttpResponse(json.dumps(ret))


# 删除操作
def delete(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        nid = request.POST.get('nid')
        models.Host.objects.filter(nid=nid).delete()
    except Exception as e:
            ret['status'] = False
            ret['error'] = "request error"
    return HttpResponse(json.dumps(ret))


# form提交数据添加操作
def app(request):
    """
    host函数通过request区别get和post方法，如果是request是get方法,就从数据库中查询数据，然后将查询的数据返回给HTML进行渲染展示
    如果是request是post方法,就从request中提取数据，然后进行数据库添加操作
    :param request:
    :return:
    """
    if request.method == "GET":
        app_list = models.Application.objects.all()
        host_list = models.Host.objects.all()
        return render(request, 'app.html', {"app_list": app_list, 'host_list': host_list})
    elif request.method == "POST":
        app_name = request.POST.get('app_name')
        host_list = request.POST.getlist('host_list')
        obj = models.Application.objects.create(name=app_name)
        obj.host.add(*host_list)

        return redirect('/app/app')


# ajax提交数据添加操作
def ajax_add_app(request):
    ret = {'status': True, 'error': None, 'data': None}
    print(request.POST)
    try:
        app_name = request.POST.get("app_name")
        host_list = request.POST.getlist('host_list')
        obj = models.Application.objects.create(name=app_name)
        obj.host.add(*host_list)
    except Exception as e:
            ret['status'] = False
            ret['error'] = "request error"

    return HttpResponse(json.dumps(ret))


# 编辑操作
def ajax_submit_edit(request):
    ret = {'status': True, 'error': None, 'data': None}
    print(request.POST)
    try:
        nid = request.POST.get("nid")
        app_name = request.POST.get("app")
        host_list = request.POST.getlist('host_list')
        obj = models.Application.objects.get(id=nid)
        obj.name = app_name
        obj.save()
        obj.host.set(host_list)
    except Exception as e:
            ret['status'] = False
            ret['error'] = "request error"
    return HttpResponse(json.dumps(ret))


# 删除操作
def ajax_submit_delete(request):
    ret = {'status': True, 'error': None, 'data': None}
    print(request.POST)
    try:
        nid = request.POST.get("nid")
        host_list = request.POST.getlist('host_id_list')
        obj = models.Application.objects.get(id=nid)
        obj.host.remove(*host_list)
        models.Application.objects.filter(id=nid).delete()
    except Exception as e:
            ret['status'] = False
            ret['error'] = "request error"
    return HttpResponse(json.dumps(ret))