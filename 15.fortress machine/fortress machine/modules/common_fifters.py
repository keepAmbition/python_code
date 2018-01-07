from models import models
from modules.db_conn import session
from modules.utils import print_err


def bind_hosts_filter(values):
    """
    根据传入参数，在bind_host表中查询数据并返回
    :param values:
    :return:
    """
    print('**>', values.get('bind_hosts'))
    bind_hosts = session.query(models.BindHost).filter(models.Host.hostname.in_(values.get('bind_hosts'))).all()
    if not bind_hosts:
        print_err("none of [%s] exist in bind_host table." % values.get('bind_hosts'), quit=True)
    return bind_hosts


def user_profiles_filter(values):
    """
    根据传入参数，在user_profile表中查询数据并返回
    :param values:
    :return:
    """
    user_profiles = session.query(models.UserProfile).filter(models.UserProfile.username.in_(values.get('user_profiles'))
                                                             ).all()
    if not user_profiles:
        print_err("none of [%s] exist in user_profile table." % values.get('user_profiles'), quit=True)
    return user_profiles