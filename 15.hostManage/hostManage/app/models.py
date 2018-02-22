from django.db import models


class Business(models.Model):
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32)


# 方式一：由Django自动创建关系表(通过Django创建的关系表，不可以直接通过类名操作关系表，只能通过间接方式操作表)
class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32, db_index=True)
    # 默认为protocol="both"，即支持ipv4,也支持ipv协议
    ip = models.GenericIPAddressField(protocol="ipv4", db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey(to="Business", to_field='id', null=True, on_delete=models.SET_NULL)


class Application(models.Model):
    name = models.CharField(max_length=32)
    host = models.ManyToManyField("Host")
