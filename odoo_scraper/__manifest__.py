{
    'name': 'Web Scraper',
    'version': '1.0',
    'category': 'Tools',
    'summary': '网页数据抓取工具',
    'description': """
        Odoo 网页数据抓取模块
        ================
        
        功能特点：
        - 配置和管理爬虫任务
        - 执行网页数据抓取
        - 存储和展示爬取结果
    """,
    'author': 'Albertsun6',
    'website': 'https://github.com/Albertsun6/odoo-scraper',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/scraper_task_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
} 