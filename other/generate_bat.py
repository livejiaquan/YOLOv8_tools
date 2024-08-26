import yaml
 
# 读取配置文件
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)
 
conda_path = config['conda_path']
env_name = config['env_name']
python_script_path = config['python_script_path']
rtsp_url = 'rtsp://admin:tkec1234@10.47.170.116:554/cam/realmonitor?channel=1&subtype=0'
 
# 生成批处理文件内容
bat_content = f"""
@echo off
 
call {conda_path}
 
call conda activate {env_name}
 
echo CAM-16-1300
 
set "source={rtsp_url}"
 
python {python_script_path} --rtsp_url="%source%"
 
echo Complete
 
pause
"""
 
# 将内容写入临时批处理文件
with open('run_temp.bat', 'w') as f:
    f.write(bat_content)