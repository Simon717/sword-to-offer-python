import requests
import time
import os
import hashlib
import os.path as osp

tar_dir = r'E:\google_landmark'
tarmd5_dir = r'E:\google_landmark\md5'
dirs = ['train', 'index', 'test']

def mkdirs(tar_dir):
    if not osp.exists(tar_dir):
        os.makedirs(tar_dir)
    for m in dirs:
        m_dir = osp.join(tar_dir, m)
        if not osp.exists(m_dir):
            os.makedirs(m_dir)
mkdirs(tarmd5_dir)
mkdirs(tar_dir)


# def get_md(path):
#     fd = open(path, "r")
#     fcont = fd.r
#     fd.close()
#     fmd5 = hashlib.md5(fcont)
#     return fmd5

def get_md(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

def down_tar(i, mode):
    url = f'https://s3.amazonaws.com/google-landmark/{mode}/images_{i:03d}.tar'
    r = requests.get(url)
    with open(osp.join(tar_dir, mode, osp.basename(url)), "wb") as code:
        code.write(r.content)
    return osp.join(tar_dir, mode, osp.basename(url))

def down_md(i, mode):
    url = f'https://s3.amazonaws.com/google-landmark/md5sum/{mode}/md5.images_{i:03d}.txt'
    r = requests.get(url)
    with open(osp.join(tarmd5_dir, mode, osp.basename(url)), "wb") as code:
        code.write(r.content)
    return osp.join(tarmd5_dir, mode, osp.basename(url))

def read_md(fn):
    with open(fn, 'r') as f:
        line = f.readline().strip().split()
    return line[0]

i = 96
def do_task(N, mode):
    # for i in range(stt, N):
    global i
    while i < N:
        stt = time.time()
        tar_fn = down_tar(i, mode)
        md_fn = down_md(i, mode)
        if get_md(tar_fn) == read_md(md_fn):
            i += 1
            print(f"{mode} {i:03d} success.. cost time {(time.time() - stt)/60:.2f} mins")
        else:
            print(f"{mode} {i:03d} md5 error.. retry...")
        # time.sleep(5)

def downmd5(N, mode, stt=0):
    def down(i):
        url = f'https://s3.amazonaws.com/google-landmark/md5sum/{mode}/md5.images_{i:03d}.txt'
        r = requests.get(url)
        with open(osp.join(tarmd5_dir, mode, osp.basename(url)), "wb") as code:
            code.write(r.content)

    for i in range(stt, N):
        down(i)
        print(f"{mode} {i:03d} completed..")
        # time.sleep(5)

def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)

def check(N, mode):
    res = []
    for i in range(N):
        path = osp.join(tar_dir, mode, f"images_{i:03d}.tar")
        size = get_FileSize(path)
        if size < 830:
            print(f"path {path} size is {size} Mb")
            res.append(i)
    return res

def redown(lst, mode):
    def down(i):
        url = f'https://s3.amazonaws.com/google-landmark/{mode}/images_{i:03d}.tar'
        r = requests.get(url)
        with open(osp.join(tar_dir, mode, osp.basename(url)), "wb") as code:
            code.write(r.content)
    for i in lst:
        down(i)
        path = osp.join(tar_dir, mode, f"images_{i:03d}.tar")
        size = get_FileSize(path)
        print(f"path {path} size is {size} Mb")


do_task(100, 'index')
# do_task(100, 'index', stt=)
# do_task(20, 'test')

# lst = check(500, 'train')
# redown(lst, 'train')

# lst = check(100, 'index')
# print('*'*20)
# redown(lst, 'index')

## 下载md5
# downmd5(500, 'train', stt=257)
# downmd5(100, 'index')
# downmd5(20, 'test')
