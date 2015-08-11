删除重复脚本使用方法(deleUnusedPhoto.sh)
该脚步使用，通常有两种方式，一种集成xcode内进行脚本执行，一种直接在终端进行执行
终端执行，更为简单和方便，因此这里简单介绍下终端内执行步骤。

前提条件:************************************************
默认采用ACK指令,终端安装指令:sudo apt-get install ack-grep;
或者可以采用Silver Search,搜索效率高;
如果采用Silver Search,先安装homebrew,然后通过brew install the_silver_searcher;同时，打开脚本，将第8行的ack改为ag;

步骤:*****************************************************
1. 打开脚本，修改imagesPath和dirPath路径,改为本地的对应路径
注意: 
    ［iamgesPath:图片路径，dirPath:搜索是否使用路径］
    ［谨慎设置dirPath，如果dirPath包含framework，会删除framework内bundle内未使用的图片资源，建议不要删除］
3. 打开终端，cd 至脚本目录
4. 启动权限，执行 chmod +x ./deleUnusedPhoto.sh
5. 输入 ./deleUnusedPhoto.sh
6. 进入所在的工程目录,去掉已删除图片的引用即可
