from odoo import models, fields, api
from datetime import datetime, timedelta
import json

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
    password = fields.Char(string='密码')  # 将通过compute方法加密
    
    # API登录配置
    api_login_url = fields.Char(string='API登录地址')
    api_params = fields.Text(string='API参数', help='JSON格式')
    
    # Cookie配置
    cookies = fields.Text(string='Cookies', help='JSON格式')
    
    # 会话管理
    session_valid = fields.Boolean(string='会话有效', default=False, compute='_compute_session_valid', store=True)
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

    @api.depends('last_login_time', 'session_timeout')
    def _compute_session_valid(self):
        """计算会话是否有效"""
        for task in self:
            if not task.last_login_time:
                task.session_valid = False
                continue
            
            timeout = timedelta(minutes=task.session_timeout)
            task.session_valid = datetime.now() - task.last_login_time < timeout

    @api.onchange('need_login')
    def _onchange_need_login(self):
        """当需要登录变化时，更新状态"""
        if self.need_login and self.state == 'ready':
            self.state = 'login_required'
        elif not self.need_login and self.state == 'login_required':
            self.state = 'ready'

    @api.onchange('login_type')
    def _onchange_login_type(self):
        """当登录类型变化时，清空其他登录方式的字段"""
        if self.login_type == 'form':
            self.api_login_url = False
            self.api_params = False
            self.cookies = False
        elif self.login_type == 'api':
            self.login_url = False
            self.username_field = False
            self.password_field = False
            self.username = False
            self.password = False
            self.cookies = False
        elif self.login_type == 'cookie':
            self.login_url = False
            self.username_field = False
            self.password_field = False
            self.username = False
            self.password = False
            self.api_login_url = False
            self.api_params = False

    def validate_json_field(self, field_value, field_name):
        """验证JSON格式字段"""
        if not field_value:
            return True
        try:
            json.loads(field_value)
            return True
        except json.JSONDecodeError:
            raise ValueError(f"{field_name}必须是有效的JSON格式")

    @api.constrains('api_params', 'cookies')
    def _check_json_fields(self):
        """检查JSON格式字段的有效性"""
        for record in self:
            if record.api_params:
                record.validate_json_field(record.api_params, 'API参数')
            if record.cookies:
                record.validate_json_field(record.cookies, 'Cookies') 