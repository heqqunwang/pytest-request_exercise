global_env = {}

def pytest_addoption(parser):
    ##hook函数，是添加命令行参数使用
    # group 将下面所有的 option都展示在这个group下。
    mygroup = parser.getgroup("hogwarts")
    # 注册一个命令行选项
    mygroup.addoption("--env",
     # 参数的默认值
    default='test_env',
    # 存储的变量
    dest='env',
    # 参数的描述信息
    help='设置接口自动化测试默认的环境'
     )

def pytest_configure(config):
    ##获取设置的命令行参数，并传给变量global_env
    default_ev = config.getoption("--env")
    tmp = {"env": default_ev}
    global_env.update(tmp)