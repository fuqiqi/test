@classmethod
    def zt_new_login(cls, r_session, user_id, name=None, password=None):
        """登陆禅道
        :param r_session:会话
        :param user_id:用户id
        :param name:账号
        :param password:密码
        :return:
        """
        # 查询当前用户的数据
        user_name = ''
        user_password = ''
        # if user_id != 0:
        #     result_user = User.query.filter(User.id == user_id).first()
        #     if result_user.ext:
        #         user_name = result_user.name
        #         user_password = Validation.aes_decrypt(result_user.ext)
        # else:
        if name and password:
            user_name = name
            user_password = password
        else:
            user_name = cls.zt_user
            user_password = cls.zt_password
        
        login_params = cls.__query_params_new('user', 'login', 'json')
        response_url = r_session.get(cls.zt_base_url, params=login_params).url
        
        headers = cls.zt_headers
        headers['Referer'] = response_url
        
        body = {
            'account': user_name,
            'password': user_password,
            'keepLogin[]': 'on',
            'referer': '/zentao/',
            'verifyRand': 2035112972
        }
        
        login_response = r_session.post(url=response_url, data=body, headers=headers)
        if login_response.status_code != 200 or login_response.json()['status'] != 'success':
            raise Exception('禅道登录失败，请检查账号')
        return login_response.json()