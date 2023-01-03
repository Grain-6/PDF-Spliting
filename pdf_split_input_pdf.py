# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 14:24:42 2022

@author: Grain
"""
from PyPDF2 import PdfFileReader, PdfFileWriter #pdf库
import os #操作系统库
from natsort import ns, natsorted #自然排序库

print(r'该程序用于对扫描件合集根据pdf原文件的文件名和页数进行拆分')
print(r'目录输入格式示例：D:\债承底稿\xxx\第三期')
print(r'文件输入格式示例：D:\债承底稿\xxx\第三期\扫描件.pdf')
print(r'可在资源管理器中将目标文件或目录拖入程序框图内进行输入')
print(r'若需要复制粘贴可在左上角cmd属性中进行设置')
print(r"注意输入时请勿带有 '' 若有需手动删除!")
print(r"例如：'D:\债承底稿\xxx\第三期\扫描件.pdf'")
print(r"需要改为：D:\债承底稿\xxx\第三期\扫描件.pdf")
print('\n')

pdf_dir=input("请输入pdf文档所在目录：")

collected=input("请输入扫描文件：")

save_path=input("请输入拆分后的pdf保存目录：")

print('\n')

#r表示原来的，不然‘\’会报错

def get_filelists(file_dir):
    """    
    得到指定目录下的文件名列表（过滤掉文件夹），并按Windows的系统名称排序

    Parameters
    ----------
    file_dir : str
        文件夹所在目录.

    Returns
    -------
    filelists : list
        文件名列表.

    """
    if not file_dir: file_dir='.' #如果是空路径，则返回当前路径
    list_directory = os.listdir(file_dir)
    filelists = []
    for directory in list_directory:
        if(os.path.isfile(file_dir+'\\'+directory)): #过滤掉文件夹，只保留文件
            filelists.append(directory)
    filelists = natsorted(filelists,alg=ns.PATH)#要加alg=ns.PATH参数才和windows系统名称排序一致    
    return filelists

#---------------------------------------------------
filenames=get_filelists(pdf_dir) #得到文件名列表（过滤掉文件夹）

try:
    n=0 #起始索引
    for i in range(len(filenames)):
        this_page=PdfFileReader(pdf_dir+'\\'+filenames[i])
        nums=this_page.numPages #得到当前文件的页数
        print('正在拆分: '+filenames[i]+ ' 页数：'+str(nums))
            
        #读取合集
        pdf_reader = PdfFileReader(collected)
        
        pdf_writer = PdfFileWriter() #每一次都要重新实例化对象
        for j in range(n,n+nums): #起始索引和页数
            pdf_writer.addPage(pdf_reader.getPage(j))
        with open(save_path+'\\'+filenames[i], 'wb') as fh: 
            pdf_writer.write(fh) #输出文件
        n+=nums #起始索引移动到下一个文件开头
        
    print('拆分成功！请务必核对是否正确！')
    input('按任意键退出')

except Exception as e:
    print('程序出错')
    print(e.args) #出现错误则返回完整的错误信息
    input('按任意键退出')


