# coding: utf-8

import os
import sys
import pexpect



def ssh_connect(conf):
    """ Function doc

    @param PARAM: DESCRIPTION
    @return RETURN: DESCRIPTION
    """
    print("连接信息:" + str(conf))
    cmd = "ssh {}@{} -p {}".format(conf["name"], conf["host"], int(conf["port"]))
    child = pexpect.spawn(cmd)
    i = child.expect([".*password.*", ".*continue.*?", pexpect.EOF, pexpect.TIMEOUT])
    if( i == 0 ):
        # 如果交互中出现.*password.*，就是叫我们输入密码
        # 我们就把密码自动填入下去
        child.sendline("{}\n".format(conf["password"]))
        child.interact()
    elif( i == 1):
        # 如果交互提示是否继续，一般第一次连接时会出现
        # 这个时候我们发送"yes"，然后再自动输入密码
        child.sendline("yes\n")
        child.sendline("{}\n".format(conf["password"]))

        #child.interact()
    else:
        # 连接失败
        print("[Error]The connection fails")

conf = {}
conf["host"] = sys.argv[1]
conf["port"] = sys.argv[2]
conf["name"] = sys.argv[3]
conf["password"] =sys.argv[4]
ssh_connect(conf)

