# -*- coding: utf-8 -*-
import os
import time
import platform
import six 
import subprocess
current_file_direction = os.path.split(os.path.realpath(__file__))[0]


def execute_shell_command(command):
    """
    执行shell命令, 返回状态码和命令输出(标准输出和错误汇合至一起输出)
    兼容python2&python3
    :param command: str, shell 命令
    :return: code, stdout
    """
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout_data, _ = p.communicate()
    if type(stdout_data) == bytes:
        stdout_data = stdout_data.decode("utf-8") if six.PY2 else str(stdout_data, encoding="utf-8")
    return p.returncode, stdout_data 


def timestamp2day(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y%m%d', timeStruct)


def get_creation_day(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        t = os.path.getctime(path_to_file)
    else:
        # https://linuxize.com/post/stat-command-in-linux/
        _, stat_str = execute_shell_command('stat -f="%B" {}'.format(path_to_file))
        try:
            t = float(stat_str.strip()[-10:])
        except:
            stat = os.stat(path_to_file)
            try:
                t = stat.st_birthtime
            except AttributeError:
                # We're probably on Linux. No easy way to get creation dates here,
                # so we'll settle for when its content was last modified.
                t = stat.st_mtime
    return timestamp2day(t)


def get_modification_day(path_to_file):
    t = os.path.getmtime(path_to_file)
    return timestamp2day(t)


def load_template_file(path_to_file):
    fp = file(path_to_file)
    lines = []
    for line in fp:
        lines.append(line)
    fp.close()
    return lines


def process():
    lines = load_template_file(os.path.join(current_file_direction, "index_template.html"))
    LINE = -1
    for i, line in enumerate(lines):
        if '</body>' in line: 
            LINE = i
            break

    relative_posts_dir = "./posts/"
    posts_dir = os.path.join(current_file_direction, relative_posts_dir)

    prefix0 = '        <div class="link-class"><a href="{}'.format(relative_posts_dir)
    prefix1 = '">'
    prefix2 = '</a>'
    prefix3 = '</div>'

    files_name = os.listdir(posts_dir)
    files_html = []
    for f_name in files_name:
        if os.path.splitext(f_name)[1]=='.html':
            files_html.append(f_name)
    for f_html in files_html:
        f_md = os.path.join(posts_dir, "src", os.path.splitext(f_html)[0] + ".md")
        try:
            creation_day = str(get_creation_day(f_md))
            modification_day = str(get_modification_day(f_md))
        except Exception as e:
            print(e)
            print(os.path.join(posts_dir, f_html))
        time_info = [creation_day, modification_day]
        lines.insert(LINE, \
                    prefix0 + f_html + \
                    prefix1 + f_html[:-5] + prefix2 + \
                    "（ " + " -> ".join(time_info) + " ）" + prefix3)

    s = '\n'.join(lines)
    fp = file(os.path.join(current_file_direction, 'index.html'), 'w')
    fp.write(s)
    fp.close()


if __name__ == "__main__":
    process()