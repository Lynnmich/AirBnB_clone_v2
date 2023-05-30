#!/usr/bin/python3
""""A Fabric script that distributes an archive to web servers"""

from fabric.api import *
import os

env.hosts = ['54.90.37.210', '100.25.137.138']


def do_deploy(archive_path):
    """Archive distribution"""
    if not os.path.exists(archive_path):
        print('File does not exist')
        return False

    try:
        arc_tgz = os.path.basename(archive_path).replace('.tgz', '').replace('.tar.gz', '')

        # Upload archive to the server
        put(archive_path, '/tmp')

        # Create folder paths
        uncomp_fold = '/data/web_static/releases/{}'.format(arc_tgz)
        tmp_location = '/tmp/{}'.format(os.path.basename(archive_path))

        # Extract archive and move files
        run('mkdir -p {}'.format(uncomp_fold))
        run('tar -xzf {} -C {}'.format(tmp_location, uncomp_fold))
        run('rm {}'.format(tmp_location))
        run('mv {}/web_static/* {}'.format(uncomp_fold, uncomp_fold))
        run('rm -rf {}/web_static'.format(uncomp_fold))

        # Remove and create symbolic link
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(uncomp_fold))
        run('sudo service nginx restart')
        return True

    except Exception as err:
        print(err)
        return False


def deploy():
    """Pack and deploy all files"""
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
