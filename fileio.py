# -*- coding: utf-8 -*-
"""
fileio.py
Created on Thu Apr 18 17:28:37 2019

@author: madhu
"""
import os, shutil, glob

try:
    print('-'*30)
    cwd = r'C:\max\PyStuf\IntroPy' 
    os.chdir(cwd)

    dirpath = os.getcwd()
    foldername = os.path.basename(dirpath)
    dir_list = os.listdir('.')
    file_names = ','.join(dir_list)

    filename = 'oops.txt'
    fout = open(filename, 'wt')
    abs_path = os.path.abspath(filename)

    mesg = '''Oops, I created file {0} in directory {1}.
    Absolute path name is: {2}.
    Directory name is: {3}.
    It already had the files: {4}
    '''.format(filename, dirpath, abs_path, foldername, file_names)
    print(mesg, file=fout)
    print(mesg)
    fout.close()
    
#%%
    print('-'*30)
    i = 0
    if os.path.exists('..'):
        print('\t'*i,'.. exists.'); i += 1
    if os.path.exists('.'):
        print('\t'*i,'. exists.'); i += 1
    if os.path.exists(filename):
        print('\t'*i,filename,'exists.'); i += 1
    if os.path.exists('./'+filename):
        print('\t'*i,'./'+filename,'exists.'); i += 1
    if not os.path.exists('waffles'):
        print('\t'*i,'no waffles','exists.'); i += 1
    
#%%
                        
#%%
    print('-'*30)
    i = 0
    if os.path.isfile(filename):
        print('\t'*i,filename,'is a file.'); i += 1
    if os.path.isdir('.'):
        print('\t'*i,'.','is a directory.'); i += 1
    if not os.path.isdir(filename):
        print('\t'*i,filename,'is not a directory'); i += 1
    if os.path.isabs('/big/fake/file-name'):
        print('\t'*i,'/big/fake/file-name','is absolute path.'); i += 1
    if not os.path.isabs('big/fake/name/without/a/leading/slash'):
        print('\t'*i,'big/fake/name/without/a/leading/slash','is NOT an absolute path.'); i += 1

#%%

#%%
    print('-'*30)
    i = 0
    fil2name = 'ohno.txt'
    if fil2name == shutil.copy(filename, fil2name):
        print('\t'*i,'Copied',filename, 'to',fil2name); i += 1
        fil3name = 'ohwell.txt'
        if os.path.exists(fil3name): 
            os.remove(fil3name)
            print('\t'*i, fil3name, 'already exists, hence deleted it.'); i += 1
        os.rename(fil2name, fil3name)
        if os.path.exists(fil3name):
            print('\t'*i,'Renamed',fil2name,'to',fil3name); i += 1
            os.remove(fil3name)
            if not os.path.exists(fil3name):
                print('\t'*i,'Deleted',fil3name); i += 1
#%%

#%%
    print('-'*30)
    i = 0
    filter = 'm*'
    select_list = glob.glob(filter)
    print('\t'*i,'Selected for', filter, ':\n', select_list); i += 1
    filter = 'm??????e.*'
    select_list = glob.glob(filter)
    print('\t'*i,'Selected for', filter,  ':\n', select_list); i += 1
    filter = '[klm]*e.*'
    select_list = glob.glob(filter)
    print('\t'*i,'Selected for', filter,  ':\n', select_list); i += 1

#%%


#%%
    print('-'*30)
    i = 0
    foldr2name = 'test_folder'
    if os.path.exists(foldr2name): 
        os.rmdir(foldr2name)
        print('\t'*i, 'folder',foldr2name, 'already exists, hence deleted it.'); i += 1
    os.mkdir(foldr2name)
    if os.path.exists(foldr2name):
        print('\t'*i,'Created folder',foldr2name); i += 1
        os.rmdir(foldr2name)
        print('\t'*i, 'Deleted folder',foldr2name); i += 1

#%%

except:
    print('Sorry, error in file i/o')