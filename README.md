**简单介绍**
    Celery 是一个异步任务队列。一个Celery安装有三个核心组件：
    
    Celery 客户端: 用于发布后台作业。当与 Flask 一起工作的时候，客户端与 Flask 应用一起运行。
    
    Celery workers: 运行后台作业的进程。Celery 支持本地和远程的 workers，可以在 Flask 服务器上启动一个单独的 worker，也可以在远程服务器上启动worker，需要拷贝代码；
    
    消息代理: 客户端通过消息队列和 workers 进行通信，Celery 支持多种方式来实现这些队列。最常用的代理就是 RabbitMQ 和 Redis。
    
