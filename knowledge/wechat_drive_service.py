import requests
import base64

class WeDriveService:
    def __init__(self, corpid, corpsecret):
        self.corpid = corpid
        self.corpsecret = corpsecret
        self.access_token = None

    def get_access_token(self):
        # 获取access_token
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": self.corpid,
            "corpsecret": self.corpsecret
        }
        response = requests.get(url, params=params)
        result = response.json()
        if result.get("errcode") == 0:
            self.access_token = result["access_token"]
        else:
            raise Exception(f"获取access_token失败: {result}")

    def create_space(self, space_name):
        """
        创建微盘空间
    
        当access_token不存在时，先获取access_token
        创建空间的API接口需要POST请求，请求体包括空间名称、权限信息等
        如果access_token过期导致创建失败，重新获取access_token并重试
    
        参数:
        space_name (str): 要创建的空间的名称
    
        返回:
        dict: 创建空间的结果，包括错误码和错误信息等
        """
        # 创建微盘空间
        if not self.access_token:
            self.get_access_token()
        
        url = "https://qyapi.weixin.qq.com/cgi-bin/wedrive/space_create"
        params = {"access_token": self.access_token}
        payload = {
            "space_name": space_name,
            "auth_info": [{
                "type": 1,
                "userid": "penglang@xun-ao.com",
                "auth": 7
            }],
            "space_sub_type": 0
        }
        
        print(f"请求 URL: {url}, 参数: {params}, 负载: {payload}")  # 添加调试信息
        
        response = requests.post(url, params=params, json=payload)
        result = response.json()
        
        print(f"响应结果: {result}")  # 添加调试信息
        
        # 处理access_token过期的情况
        if result.get("errcode") == 40014:
            self.get_access_token()  # 重新获取token
            return self.create_space(space_name)  # 重试请求
        
        return result

    def update_space(self, space_id):
        # 修改微盘空间
        if not self.access_token:
            self.get_access_token()
        
        url = "https://qyapi.weixin.qq.com/cgi-bin/wedrive/space_acl_add"
        params = {"access_token": self.access_token}
        payload = {
            "spaceid": space_id,
            "auth_info": [{
                "type": 1,
                "userid": "penglang@xun-ao.com",
                "auth": 7
            }, {
                "type": 1,
                "userid": "xiongxing@xun-ao.com",
                "auth": 1
            }]
        }
        
        response = requests.post(url, params=params, json=payload)
        result = response.json()
        
        # 处理access_token过期的情况
        if result.get("errcode") == 40014:
            self.get_access_token()  # 重新获取token
            return self.update_space(space_id)  # 重试请求
        
        return result

    def upload_file(self, space_id, file_path, file_name):
        # 上传文件到微盘
        if not self.access_token:
            self.get_access_token()
        
        url = "https://qyapi.weixin.qq.com/cgi-bin/wedrive/file_upload" 
        params = {"access_token": self.access_token}
        payload = {
            "spaceid": space_id,
            "fatherid": space_id,
            "file_name": file_name,
            "file_base64_content": self.get_file_base64(file_path)
        }
        response = requests.post(url, params=params, json=payload)
        result = response.json()
        
        print(f"响应结果: {result}")  # 添加调试信息
        
        return result
    
    def get_file_list(self, space_id):
        # 获取文件列表
        if not self.access_token:
            self.get_access_token()

        url = "https://qyapi.weixin.qq.com/cgi-bin/wedrive/file_list"
        params = {"access_token": self.access_token}
        payload = {
            "spaceid": space_id,
            "fatherid": space_id,
            "sort_type": 1,
            "start": 0,
            "limit": 100
        }
        response = requests.post(url, params=params, json=payload)
        result = response.json()
        return result

    def download_file(self, file_id):
        if not self.access_token:
            self.get_access_token()

        # 下载文件
        url = "https://qyapi.weixin.qq.com/cgi-bin/wedrive/file_download"
        params = {"access_token": self.access_token}
        payload = {
            "fileid": file_id
        }
        response = requests.post(url, params=params, json=payload)
        result = response.json()
        return result

    def download_file_by_url(self, file_url, cookies=None, save_path=None):
        # 下载文件
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(file_url, headers=headers, cookies=cookies)
        
        # 检查响应状态码
        if response.status_code == 200:
            # 如果指定了保存路径，则将文件保存到指定路径
            if save_path:
                with open(save_path, "wb") as file:
                    file.write(response.content)
                return f"文件已保存到: {save_path}"
            else:
                # 返回文件内容
                return response.content
        else:
            raise Exception(f"文件下载失败，状态码: {response.status_code}")
                
        
    def get_file_base64(self, file_path):
        # 获取文件的base64编码
        with open(file_path, "rb") as file:
            return base64.b64encode(file.read()).decode("utf-8")

# 使用示例
if __name__ == "__main__":
    # 需要从企业微信后台获取以下参数
    service = WeDriveService(
        corpid="wwed84b05eb31f6f6e",
        corpsecret="9TbmYxmqUY10PQZqmkCQOzoMWtCr_9XYy3EGg0DjwKs"
    )
    
    # try:
    #     result = service.create_space(
    #         space_name="彭朗的测试空间"
    #     )
    #     print("创建结果:", result)
    # except Exception as e:
    #     print("操作失败:", str(e)) s.wwed84b05eb31f6f6e.742960305VE0

    # try:
    #     result = service.update_space(
    #         space_id="s.wwed84b05eb31f6f6e.742960305VE0"
    #     )
    #     print("创建结果:", result)
    # except Exception as e:
    #     print("操作失败:", str(e))

    # try:
    #     result = service.upload_file(
    #         space_id = "s.wwed84b05eb31f6f6e.742960305VE0",
    #         file_path = "./1.pdf",
    #         file_name= "deepseek从入门到精通.pdf"
    #     )
    #     print("创建结果:", result)
    # except Exception as e:
    #     print("操作失败:", str(e))

    # try:
    #     result = service.get_file_list(
    #         space_id = "s.wwed84b05eb31f6f6e.742960305VE0"
    #     )
    #     print("创建结果:", result)
    # except Exception as e:
    #     print("操作失败:", str(e))  

    # try:
    #     result = service.download_file(
    #         file_id = "s.wwed84b05eb31f6f6e.742960305VE0_f.742968425DLa2"
    #     )
    #     print("创建结果:", result)
    # except Exception as e:
    #     print("操作失败:", str(e))

    try:
        result = service.download_file_by_url(
            file_url = "https://szfront.wxwork.qq.com/downloadobject?fileid=08011204313330332210353632393530323831383735383438382a0131322461616439653566322d303666392d343232302d626337322d3462303532643865623738353899c49b0942148590a319d3c2b370b6cbf4ec4809051eac2ff8f048015802600768b8177207333030303030309001e9ac8ebf069a0100a001d1e002&filename=deepseek%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E7%B2%BE%E9%80%9A.pdf",
            cookies = {
                "authkey": "70080010091870227054f804ac9ad80ce1a0b7f8cca430a715f864c405c9fdd82af960b7941dd7b1fcbc728b1b8d540b65c344fc4294b70c890de452e308e63b27803ce34915cfb5f3caf656c2f01b9c59573ffaae812982a758aa25241a5e8bc084691b6a1e42f463a4629f683d2a4fb111269460118f8ae5&weixinnum=5629502818758488"
            },
            save_path = "./deepseek.pdf"
        )
        print("创建结果:", result)
    except Exception as e:
        print("操作失败:", str(e))