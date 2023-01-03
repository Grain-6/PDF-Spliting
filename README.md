# PDF-Spliting
This program is used to split the scanned copy collection according to the file name and page number of the original pdf or word file.

pdf_split_input_pdf.py is used to split the original word file
pdf_split_input_word.py is used to split the original pdf file
Prioritize using the original pdf file for splitting

Be sure to check the following before splitting:
1. The order when printing the original file is "Sort by name (ascending order)" in Windows Explorer
2. There are no blank pages in the scanned document collection
3. The total number of pages of the original document and the scanned copy is the same (if the original document is in word format, the number of pages in word and the number of pages in pdf may be different)
4. There are no other files in the directory where the original file is located

After the split is successful, please be sure to check manually!

Example of directory input format: D:\Debt Commitment Draft\xxx\Phase 3
Example of file input format: D:\Debt commitment draft\xxx\third issue\scanned copy.pdf
In the resource manager, the target file or directory can be dragged into the block diagram for input
If you need to copy and paste, you can set it in the cmd attribute in the upper left corner
Be careful not to enter with '' if you need to delete it manually!
For example: 'D:\Debt commitment paper\xxx\third phase\scanned copy.pdf'
It needs to be changed to: D:\Debt Undertaking Draft\xxx\Third Issue\Scanned Copy.pdf

pdf_split_input_pdf.exe 用于拆分原文件为word

pdf_split_input_word.exe 用于拆分原文件为pdf

优先使用原文件为pdf的情况进行拆分

拆分前请务必进行如下检查：
1.打印原文件时的顺序为Windows资源管理器中的"按名称排序（升序排列）"

2.扫描件合集没有空白页

3.原文件和扫描件总页数一致（若原文件为word格式，可能出现word的页数和pdf页数不同的情况）

4.原文件所在目录下没有其他文件

拆分成功后请务必人工查验！

目录输入格式示例：D:\债承底稿\xxx\第三期

文件输入格式示例：D:\债承底稿\xxx\第三期\扫描件.pdf

可在资源管理器中将目标文件或目录拖入程序框图内进行输入

若需要复制粘贴可在左上角cmd属性中进行设置

注意输入时请勿带有 '' 若有需手动删除!

例如：'D:\债承底稿\xxx\第三期\扫描件.pdf'

需要改为：D:\债承底稿\xxx\第三期\扫描件.pdf
