# 爬虫模块开发任务列表

## 第一阶段：基础模块框架
1. ✅ 创建最小可安装的 Odoo 模块
   - ✅ 创建 `__manifest__.py`
   - ✅ 创建基本目录结构
   - ✅ 验证：模块可以在 Odoo 中安装和卸载
   完成时间：2024-03-27

2. ⬜ 创建爬虫任务的基本模型（当前任务）
   - 实现最简单的任务模型
   - 创建基本列表视图和表单视图
   - 验证：可以创建和查看简单的爬虫任务

建议的基本模型字段（更新版）：
```python
class ScraperTask(models.Model):
    _name = 'scraper.task'
    _description = '爬虫任务'
    
    # 基本信息
    name = fields.Char(string='任务名称', required=True)
    url = fields.Char(string='目标网址', required=True)
    active = fields.Boolean(string='启用', default=True)
    notes = fields.Text(string='备注')
    
    # 登录配置
    need_login = fields.Boolean(string='需要登录', default=False)
    login_type = fields.Selection([
        ('form', '表单登录'),
        ('api', 'API登录'),
        ('cookie', 'Cookie登录')
    ], string='登录方式', default='form')
    
    # 表单登录配置
    login_url = fields.Char(string='登录页面URL')
    username_field = fields.Char(string='用户名字段名')
    password_field = fields.Char(string='密码字段名')
    username = fields.Char(string='用户名')
    password = fields.Char(string='密码', invisible=True)  # 需要加密存储
    
    # API登录配置
    api_login_url = fields.Char(string='API登录地址')
    api_params = fields.Text(string='API参数', help='JSON格式')
    
    # Cookie配置
    cookies = fields.Text(string='Cookies', help='JSON格式')
    
    # 会话管理
    session_valid = fields.Boolean(string='会话有效', default=False)
    last_login_time = fields.Datetime(string='最后登录时间', readonly=True)
    session_timeout = fields.Integer(string='会话超时(分钟)', default=60)
    
    # 基本状态信息
    state = fields.Selection([
        ('draft', '草稿'),
        ('ready', '就绪'),
        ('login_required', '需要登录'),
        ('running', '运行中'),
        ('done', '完成'),
        ('error', '错误')
    ], string='状态', default='draft')
    
    # 时间信息
    create_date = fields.Datetime(string='创建时间', readonly=True)
    last_run_date = fields.Datetime(string='最后运行时间', readonly=True)
```

视图建议（更新版）：
1. 列表视图显示：
   - 任务名称
   - 目标网址
   - 状态
   - 需要登录
   - 会话有效
   - 最后运行时间
   - 是否启用

2. 表单视图分组：
   - 基本信息（名称、URL）
   - 登录配置（根据登录方式动态显示不同字段）
   - 状态信息
   - 备注

3. 安全性考虑：
   - 密码字段需要加密存储
   - Cookie和API参数需要安全存储
   - 添加访问权限控制

主要更新：
1. 添加了登录相关配置：
   - 支持三种登录方式：表单、API、Cookie
   - 每种登录方式的具体配置字段
   - 会话管理（有效性、超时等）

2. 扩展了状态选项：
   - 添加了 `login_required` 状态

3. 增加了安全性考虑：
   - 密码等敏感信息需要加密
   - 会话状态管理

你觉得这个设计如何？是否还需要：
1. 添加其他登录方式？
2. 添加更多的会话管理功能？
3. 添加登录失败重试机制？
4. 其他任何建议？

## 第二阶段：简单爬虫功能
3. ⬜ 实现基本的网页抓取
   - 使用 requests 实现单个 URL 抓取
   - 添加手动执行按钮
   - 验证：可以抓取指定 URL 的内容

4. ⬜ 添加数据存储
   - 创建抓取结果模型
   - 存储原始响应内容
   - 验证：可以查看抓取的原始数据

## 第三阶段：数据解析
5. ⬜ 添加选择器配置
   - 在任务模型中添加 CSS 选择器字段
   - 实现基本的数据提取逻辑
   - 验证：可以使用选择器提取数据

6. ⬜ 数据结构化存储
   - 定义结构化数据模型
   - 实现数据解析和存储
   - 验证：可以查看格式化的数据

## 第四阶段：任务管理
7. ⬜ 添加任务状态管理
   - 添加状态字段和状态转换
   - 实现状态更新逻辑
   - 验证：任务状态正确反映执行情况

8. ⬜ 添加执行日志
   - 创建日志模型
   - 记录执行过程和错误信息
   - 验证：可以查看任务执行历史

## 第五阶段：基本调度
9. ⬜ 添加定时执行
   - 添加执行计划字段
   - 实现定时任务逻辑
   - 验证：任务可以按计划自动执行

10. ⬜ 添加并发控制
    - 实现任务队列
    - 添加执行锁机制
    - 验证：多个任务可以正常排队执行

## 后续功能（待确认）
- ⬜ 代理支持
- ⬜ 数据导出
- ⬜ 更多选择器类型
- ⬜ 分页支持
- ⬜ 错误重试
- ⬜ 数据清洗规则

## 开发注意事项
1. 每完成一个任务都要进行完整测试
2. 编写必要的注释和文档
3. 保持代码简洁可维护
4. 随时收集用户反馈
5. 及时调整开发计划

## 当前任务
👉 从第一阶段第1步开始：创建最小可安装的 Odoo 模块

需要我现在就开始实现第一个任务吗？ 