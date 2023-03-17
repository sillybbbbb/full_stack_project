import xlwt
import json
import requests
from config import *

# def set_mysql(bag:dict):




def get_package(task_id):
    url = 'http://aip.nioint.com/api/metrics/metrics/hil_replay/case/table_list?exec_plan_id='+task_id+'&created=0&page_size=100&page=0'
    response = requests.get(url,cookies=cookies)
    # 检查请求状态
    if response.status_code == 200:
        # 将数据转换为字典
        data = response.json()['data']
        # case_id =        
    else:
        print("请求失败，状态码：", response.status_code)
    return data

def get_version_info(task_id):
    url2 = 'http://aip.nioint.com/api/metrics/metrics/hil_replay/new/table/list?exec_plan_id='+task_id+'&created=0&page=0'
    response = requests.get(url2,cookies=cookies)
    if response.status_code == 200:
        # 将数据转换为字典
        data_exec =response.json()['data']
        version = data_exec['content'][0]['exec_config']
        version_json = json.loads(version)
        # version_url = version_json['mazu_debug_url']
        # version_name = version_json['dailysim_version'].split('/')[-1]+'_'+version_json['region']
        return version_json      
    else:
        print("请求失败，状态码：", response.status_code)


def get_cpu_detail(exec_plan_id,case_id,task_id):
    url = f'http://aip.nioint.com/api/metrics/metrics/hil/new/draw/data?exec_plan_id={exec_plan_id}&case_id={case_id}&task_id={task_id}&key=cpu_mem&'+start_end_time[case_id]+'&sample_rate=1&tab_value='
    response = requests.get(url,cookies=cookies)
    if response.status_code == 200:
        # 将数据转换为字典
        cpu_package =response.json()['data']['cpu_mem']['raw_data']
        # app_package = response.json()['data']['cpu_mem']['raw_data']['pair']
        return cpu_package
    else:
        print("请求失败，状态码：", response.status_code)
def get_network_detail(exec_plan_id,case_id,task_id):
    key = 'network_monitor'
    url = f'http://aip.nioint.com/api/metrics/metrics/hil/new/draw/data?exec_plan_id={exec_plan_id}&case_id={case_id}&task_id={task_id}&key={key}&'+start_end_time[case_id]+'&sample_rate=1&tab_value='
    response = requests.get(url,cookies=cookies)
    if response.status_code == 200:
        # 将数据转换为字典
        cpu_package =response.json()['data'][key]['raw_data']['nin1']
        return cpu_package
    else:
        print("请求失败，状态码：", response.status_code)
def get_all(bag:dict):
    if len(bag)==0:
        return {}
    ret_all = {}
    ret = {}
    error_bag = bag['common_fields'][-1]['checkers_result']

    ret_all['case_id'] = bag['case_id']
    ret_all['case_name'] = bag['case_name']
    for key,v in error_bag.items():
        if key=='topic_loss' :
            # if v['info']=={}:
            #     ret[key]="topic丢包:{}".format(v['error'])

            if v['info'] and v['info']['topic_loss_cnt']>20:
                ret[key]="topic丢包:{}".format(v['info']['topic_loss_cnt'])
            
        if key =='coredump':
            for k1,v1 in v['info']['coredumps'].items():
                if v1:
                    ret[key] = k1+'有coredump!!!'
            
        if v['error']!='':
            
            if key=='perception_framerate':
                li = []
                li=v['error'].split('；')[:-1]
                t = v['info']
                # kt = t.keys[:-4]
                for i in list(t.keys())[:-4]:
                    if 'no proto' in t[i]:
                        li.append(i+'没有感知')
                ret[key] = ';\n    '.join(li)
            elif key=='time_delay':
                continue
            elif key == 'cpu_mem':
                # ret[key]=[i.rsplit("_", 1)[0]+'超限' for i in v['info'].keys()]\
                
                    
                core = {
                    "s1":[],
                    "s2":[],
                    "s3":[],
                    "s4":[]
                }
                ans = ''
                for k2,v2 in v['info'].items():
                    
                    vt = k2.split('_')
                    if len(vt)==2:
                        core[vt[1]].append(('oom'))
                        continue
                    if len(vt)==3:
                        core[vt[1]].append((vt[0],v2))
                        continue
                    if len(vt)==4:
                        core[vt[2]].append((vt[0],'total',v2))
                        continue
                    pos = vt[-3]
                    app_name = '_'.join(vt[:-4])
                    # if (pos,app_name) not in core[vt[-4]]:
                    try:
                        core[vt[-4]].append((pos,app_name,v2,vt[-1]))
                    except:
                        pass
                    
                leak = ''
                for k3,v3 in core.items():
                    cpu = ''
                    mem = ''
                    oom = ''
                    total = ''
                    ram = ''
                    
                    for v4 in v3:
                        if v4:
                            if v4[0]=='cpu':
                                # cpu+=v4[1]+str(v4[2])+', '
                                if v4[1] == 'total':
                                    total = '_cpu_total超限({},{})'.format(v4[2][list(v4[2].keys())[0]],v4[2][list(v4[2].keys())[2]])
                                else:
                                    cpu+='{}({},{})， '.format(v4[1]+'_'+v4[3],v4[2][list(v4[2].keys())[0]],v4[2][list(v4[2].keys())[2]])
                            elif v4[0]=='mem':
                                if v4[-1]=='leak':
                                    leak += '{}({},{})， '.format(k3+'_'+v4[1]+'_'+v4[3],v4[2][list(v4[2].keys())[3]],v4[2][list(v4[2].keys())[4]])
                                elif v4[1] == 'total':
                                    total = '_mem_total超限({},{})'.format(v4[2][list(v4[2].keys())[0]],v4[2][list(v4[2].keys())[2]])
                                else:   
                                    mem+='{}({},{})， '.format(v4[1]+'_'+v4[3],v4[2][list(v4[2].keys())[0]],v4[2][list(v4[2].keys())[2]])
                            elif v4=='oom':
                                oom = '_oom超限！！！'
                            
                            # elif v4[0] == 'ram':
                            #     ram = '_ram超限({},{})'.format(v4[1][list(v4[1].keys())[0]],v4[1][list(v4[1].keys())[2]])
                            else:
                                ram = '_{}超限:({},{})'.format(v4[0],v4[1][list(v4[1].keys())[0]],v4[1][list(v4[1].keys())[2]])
                            
                            

                    if cpu:
                        ans+='      {}_cpu超限：{}\n'.format(k3,cpu[:-2])
                    if mem:
                        ans+='      '+k3+'_mem超限：'+mem[:-2]+'\n'
                    if oom:
                        ans+='      '+k3+ oom+'\n'
                    if total:
                        ans +='      '+k3+ total+'\n'
                    if ram:
                        ans += '      '+k3+ram+'\n'
                if leak:
                    ans+='      '+"内存泄露预警："+leak[:-2]+'\n'
                        
                        
                ret[key] = ans[6:-1]
            elif key == 'power_consumption':
                ans = '功耗超限：'
                for k1,v1 in v['info'].items():
                    if k1=='power_consumption':
                        continue
                    # for k2,v2 in v1.items():
                    ans+='{}({},{})， '.format(k1,v1[k1.split('_')[0]],v1['standard_'+k1.split('_')[1]])
                ret[key]=ans[:-2]
            elif key == 'network_monitor':
                ans = '网络带宽超限：'
                for k1,v1 in v['info'].items():
                    ans+='{}({},{})， '.format(k1,v1[list(v1.keys())[0]],v1[list(v1.keys())[-1]])
                ret[key]=ans[:-2]
            elif key == "cpu_top_thread_monitor":
                # system_process=['systemd','ps','sshd']
                ans = '进程算力超限：\n'
                # core = {
                #     "s1":[],
                #     "s2":[],
                #     "s3":[],
                #     "s4":[]
                # }
                sys_surpass = "      系统进程："
                deb_surpass = "      调试相关进程："
                nonsys = "      非系统相关进程："
                for k1,v1 in v['info'].items():
                    vt=k1.split('_')
                    proname = '_'.join(vt[3:-1])
                    if proname in system_proc:
                        sys_surpass+='{}_Other_{}({},{})， '.format(vt[0],proname,v1[list(v1.keys())[0]],v1[list(v1.keys())[-1]])
                    elif proname in deb_proc:
                        deb_surpass+='{}_Other_{}({},{})， '.format(vt[0],proname,v1[list(v1.keys())[0]],v1[list(v1.keys())[-1]])
                    else:
                        nonsys += '{}_Other_{}({},{})， '.format(vt[0],proname,v1[list(v1.keys())[0]],v1[list(v1.keys())[-1]])
                        # core[vt[0]].append((proname,v1))
                # ans+=sys_surpass[:-2]
                # ans +='\n      非系统进程：'
                # for k2,v2 in core.items():
                #     for v3 in v2:
                #         ans+='{}_Other_{}({},{})， '.format(k2,v3[0],v3[1][list(v3[1].keys())[0]],v3[1][list(v3[1].keys())[-1]])
                    # ans = ans[:-1]+ '\n'
                ans+= sys_surpass[:-2]+'\n'
                ans+= deb_surpass[:-2]+'\n'
                ans+= nonsys[:-2]
                ret[key]=ans

            else:
                ret[key] = v['error'].replace('\n','')
    ret_all['error'] = ret
    return ret_all

def to_excel(taskid,result):
    # 创建工作薄
    workbook = xlwt.Workbook(encoding = 'utf-8')

    # 创建工作表
    worksheet = workbook.add_sheet('Sheet1')

    # 写入数据
    
    for i in range(len(result)):
        if result[i]['errors']:
            worksheet.write(i,0,result[i]['case_name'])
            worksheet.write(i,1,result[i]['case_id'])
            worksheet.write(i,2,result[i]['errors'])

    workbook.save(taskid+'.xls')