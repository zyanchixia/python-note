#scrapy爬虫基本使用
演示html页面地址：http://python123.io/ws/demo.html
应用Scrapy爬虫框架主要是编写配置型代码
#如何从cmd进入d盘？打开cmd，输入 d:即可进入
#在cmd中输入dir可以看到d盘中所有的文件
#想要进入某个具体文件，要先输入cd，如 D:\>cd D:\pycodes回车，即可呈现D:\pycodes>

#步骤1：建立一个Scrapy爬虫工程 
选取一个目录（D:\pycodes\），然后执行如下命令：
D:\pycodes>scrapy stratproject python123demo

python123demo/    外层目录
scrapy.cfg        部署Scrapy爬虫的配置文件
python123demo/    Scrapy框架的用户自定义Python代码
__init__.py       初始化脚本
items.py          Items代码模板（继承类）
middlewares.py    Middlewares代码模板（继承类）
pipelines.py      Pipelines代码模板（继承类）
settings.py       Scrapy爬虫的配置文件
spiders/          Spiders代码模板目录（继承类）
目录结构 __pycache__/     缓存目录，无需修改

spiders/        Spiders代码模板目录（继承类）
__init__.py     初始文件，无需修改 
__pycache__/    缓存目录，无需修改

#内层目录结构  用户自定义的spider代码增加在此处

#步骤2：在工程中产生一个scrapy爬虫
进入工程目录（D:\pycodes\python123demo），然后执行如下命令：
d:\pycodes\python123demo>scrapy genspider demo python123.io
#cd.. 回到D盘目录下，然后输入 cd D:\pycodes\python123demo 回车
该命令作用：
(1)生成一个名称为demo的spider
(2)在spiders目录下增加代码文件demo.py
该命令仅用于生成demo.py，该文件也可以手工生成

#步骤3：配置产生的spider爬虫
#配置：（1）初始URL地址（2）获取页面后的解析方式

#步骤4：运行爬虫，获取网页
在命令行下，执行如下命令：
D:\pycodes\python123demo>scrapy crawl demo
demo爬虫被执行，捕获页面存储在demo.html
