from sqlalchemy import Table, Column, Integer, String, ForeignKey, UniqueConstraint, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType  #  sqalchemy_utils插件
Base = declarative_base()  # 基类

# 堡垒机用户ID和远程主机ID关联
user_m2m_bindHost = Table('user_m2m_bindHost', Base.metadata,
                          Column('userProfile_id', Integer, ForeignKey('user_profile.id')),
                          Column('bind_host_id', Integer, ForeignKey('bind_host.id')),)
# 远程主机ID和主机组ID关联
bindHost_m2m_hostGroup = Table('bindHost_m2m_hostGroup', Base.metadata,
                               Column('bindHost_id', Integer, ForeignKey('bind_host.id')),
                               Column('hostGroup_id', Integer, ForeignKey('host_group.id')),)

# 堡垒机用户ID和主机ID组关联
user_m2m_hostGroup = Table('userProfile_m2m_hostGroup', Base.metadata,
                           Column('userProfile_id', Integer, ForeignKey('user_profile.id')),
                           Column('hostGroup_id', Integer, ForeignKey('host_group.id')),)


class BindHost(Base):
    """
    远程主机跟远程主机账号密码表关联
    192.168.1.11 web
    192.168.1.11 mysql
    """
    __tablename__ = "bind_host"
    # UniqueConstraint联合唯一
    __table_args__ = (UniqueConstraint('host_id', 'remoteUser_id', name='_host_remoteUser_uc'),)

    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('host.id'))
    remoteUser_id = Column(Integer, ForeignKey('remote_user.id'))
    # 外键关联远程主机，反向查绑定的主机
    host = relationship('Host', backref='bind_hosts')
    # 外键关联堡垒机用户,反向查绑定的堡垒机用户
    remote_user = relationship("RemoteUser", backref='bind_hosts')

    def __repr__(self):
        return "<host_ip:%s -- remote_user.username:%s >" % (self.host.ip, self.remote_user.username)


class RemoteUser(Base):
    """
    远程主机账号密码表
    """
    __tablename__ = 'remote_user'
    #  联合唯一,验证类型,用户名密码
    __table_args__ = (UniqueConstraint('auth_type', 'username', 'password', name='_user_password_uc'),)
    id = Column(Integer, primary_key=True)
    AuthTypes = [
        ('ssh-password', 'SSH/Password'),  # 第一个是存在数据库里的,第二个是展示给用户的看的值，这是orm的映射关系
        ('ssh-key', 'SSH/KEY')
    ]
    auth_type = Column(ChoiceType(AuthTypes))
    username = Column(String(32))
    password = Column(String(128))

    def __repr__(self):
        return "remote user:%s" % self.username


class Host(Base):
    """
    远程主机表
    """
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(64), unique=True)
    ip = Column(String(64), unique=True)
    port = Column(Integer, default=22)

    def __repr__(self):
        return "host:%s" % self.hostname


class HostGroup(Base):
    """
    远程主机组
    """
    __tablename__ = 'host_group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    # 通过bindHost_m2m_hostGroup 关联BindHost和主机组 反查到BindHost中的主机信息
    bind_hosts = relationship("BindHost", secondary="bindHost_m2m_hostGroup", backref="host_groups")

    def __repr__(self):
        return self.name


class UserProfile(Base):
    """
    堡垒机用户密码表
    """
    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    password = Column(String(128))

    # 多对多关联, 通过user_m2m_bindHost表 能反查到堡垒机用户
    bind_hosts = relationship("BindHost", secondary='user_m2m_bindHost', backref='user_profiles')
    # 多对多关联，通过userProfile_m2m_hostGroup表，能反查到堡垒机用户
    host_groups = relationship("HostGroup", secondary='userProfile_m2m_hostGroup', backref='user_profiles')

    def __repr__(self):
        return self.username


class AuditLog(Base):
    """
    用户操作日志表
    """
    __tablename__ = 'audit_log'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_profile.id'))
    bind_host_id = Column(Integer, ForeignKey('bind_host.id'))
    action_choices = [
        (u'cmd', u'CMD'),
        (u'login', u'Login'),
        (u'logout', u'Logout'),
    ]
    action_type = Column(ChoiceType(action_choices))
    # 命令字节可能很多
    # cmd = Column(String(255))
    cmd = Column(Text(65535))
    date = Column(DateTime)

    user_profile = relationship("UserProfile")
    bind_host = relationship("BindHost")