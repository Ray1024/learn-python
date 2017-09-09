#!/usr/bin/python
#Filename: backup_ver1.py

import os
import time

#1.The files and directories to be backed up are specified in a list.
source = [
        '/home/Raymond/codes_python/test_backup/dir1',
        '/home/Raymond/codes_python/test_backup/dir2'
        ]
#If you are using Windows, use source = [r'C:\Documents',r'D:\Work'] or something like that

#2.The backup must be stored in a main backup directory
target_dir = '/home/Raymond/codes_python/test_backup/backup/' #Remember to change this to what you will be using

today = target_dir + time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")

comment = raw_input('Enter a comment-->')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'
    print 'target is : ' ,target

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today

#5.We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = 'zip -q "%s" %s'% (target, ' '.join(source))
print zip_command

#Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'
