# 打开多个文件
def open_all(mod, files):
    file = {}
    for f in files:
        file[f] = open(f, mod)
    return file


# 刷新多个文件
def flushall(files):
    for key, value in files.items():
        value.flush()


# 关闭多个文件
def closeall(files):
    for key, value in files.items():
        value.close()
