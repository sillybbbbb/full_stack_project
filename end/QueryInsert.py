from mydatabase import *
import json
from util import *


def read_history(mydb:MyDatabase,path):
    with open(path,'r',encoding='utf8')as fp:
        his_data = json.load(fp)
    for version,his in his_data.items():
        print(version)
        for Day,task_id in his.items():
            if task_id:
                print(task_id)

                deal_one_task(mydb,version,Day,task_id)
def deal_power_consumption(mydb:MyDatabase,id,value):
    for k,v in value['info']['power_consumption'].items():
        mydb.add_to_power(id,int(k[1]),v['Main Power'],v['Secondary Power'])
    
def deal_perception_framerate(mydb:MyDatabase,id,value):
    def f(key):
        
        return 0 if key not in list(value['info'].keys()) or  "no proto data" in value['info'][key] else value['info'][key]['average_freq'] 
    # value['info']['common-perception-vision_road_detection']
    'common-perception-vision_road_detection'
        #   value['info']['common-perception-perception_objects_prod']
    common_perception_perception_objects_prod= f('common-perception-perception_objects_prod')
    common_perception_vision_road_detection_prod= f('common-perception-vision_road_detection')
    common_perception_vision_feature_flag_prod = f('common-perception-vision_feature_flag')
    common_perception_vision_perception_objects_prod = f('common-perception-vision_perception_objects')
    common_perception_od_output_adb_prod = f('common-perception-od_output_adb')
    common_perception_od_output_adp_prod=f('common-perception-od_output_adp') 
    common_perception_od_output_prod = f('common-perception-od_output_prod')
    common_perception_od_output_lidar_prod = f('common-perception-od_output_lidar_prod')
    common_perception_svc_perception_prod=f('common-perception-svc_perception_prod')
    common_perception_svc_nn_output = f('common-perception-svc_nn_output')
    coapp_common_perception_perception_objects = f('coapp-common-perception-perception_objects')
    coapp_common_perception_vision_road_detection = f('coapp-common-perception-vision_road_detection')
    coapp_common_perception_od_output = f('coapp-common-perception-od_output')
    mydb.add_to_perception_framerate(id,common_perception_perception_objects_prod, common_perception_vision_road_detection_prod, common_perception_vision_feature_flag_prod, common_perception_vision_perception_objects_prod, common_perception_od_output_adb_prod, common_perception_od_output_adp_prod, common_perception_od_output_prod, common_perception_od_output_lidar_prod, common_perception_svc_perception_prod, common_perception_svc_nn_output, coapp_common_perception_perception_objects, coapp_common_perception_vision_road_detection, coapp_common_perception_od_output)


def deal_thread(mydb:MyDatabase,id,value):
    for service,v1 in value['checker_extra_info'].items():#k1 = service/arg_app                
                    for v2 in v1:
                        core = int(v2['type'][1])
                        for v3 in v2['module']:
                            module_name = v3['module_name']
                            
                                
                            for app in v3['value']:
                                category = app['category']
                                # thread_name = f"{core}_{k1}_{module_name}_{category}"
                                mydb.add_to_app(id,core,service,module_name,category,app['thd_num'],app['min'],app['mean'],app['max'])

def deal_cpu_detail(mydb:MyDatabase,id,package):
    for k,v in package['solo'].items():
        tmp_list = k.split('_')
        mydb.add_to_cpu(id,int(tmp_list[-1][-1]),tmp_list[0],v['mean'],v['max'])
    for k,v in package['pair'].items():
        core=k[-1]
        app_name = k[:-3]
        mydb.add_to_proc(id,int(core),app_name,'cpu',v['cpu_use']['mean'],v['cpu_use']['max'])
        mydb.add_to_proc(id,int(core),app_name,'mem',v['mem_use']['mean'],v['cpu_use']['max'])

        



def deal_network(mydb:MyDatabase,id,package):
    for k,v in package.items():
        for k1,v1 in v.items():
            if isinstance(v1, dict):
                tmp_list = k1.split('_')
                app = tmp_list[0]
                rxtx = tmp_list[1][:2]
                kbpck = tmp_list[1][2:]               
                mydb.add_to_network(id,k,app,rxtx,kbpck,v1['mean'],v1['max'])

def deal_one_task(mydb:MyDatabase,version,date,task_id):
    # version_json=get_version_info(task_id)

    # version_name = version_json['dailysim_version'].split('/')[-1]
    region = version.split('_')[-1]
    version_name = version
    bags = get_package(task_id)
    info = ""
    for bag in bags['content']:
        # errors = get_all(bag)
        try:
            case_id = bag['case_id']
            if bag['common_fields'][-1]['checkers_result']:
                
                exec_plan_id = bag['common_fields'][-1]['id']
                cpu_package = get_cpu_detail(task_id,case_id,exec_plan_id)
                
                network_package = get_network_detail(task_id,case_id,exec_plan_id)
                errors = bag['common_fields'][-1]['checkers_result']
                if errors=={}:
                    continue
                scene = bag['case_name'].split('_')[-1]
                id = date.replace('-','')+'_'+task_id+'_'+scene

                mydb.add_to_case(id,date,region,version_name,scene,task_id)
                deal_power_consumption(mydb,id,errors['power_consumption'])
                deal_perception_framerate(mydb,id,errors['perception_framerate'])
                # deal_thread(mydb,id,errors['cpu_top_thread_monitor'])
                deal_cpu_detail(mydb,id,cpu_package)
                deal_network(mydb,id,network_package)
                info+=id+'添加完成！\n'
        except Exception as e:
            info+= str(e)+'\n'
    return info



if __name__ == '__main__':
    my = MyDatabase(host="localhost",
    user="root",
    password="123456",
    database="hil_db")
    my.connect()
    case_list_path ='end/case_list.json'


    read_history(my, case_list_path) 
# deal_one_task(my,'ad1.4.1_cn',"2023-03-15","6410b3e10cfee74df7cdc9fc")

# my.query_version_compare(['master','ad1.4.1','ad1.5.0'],'normal','2023-03-03',['common_perception_perception_objects_prod', 'common_perception_vision_road_detection'])
# my.query_version_compare('master','ad1.4.1','normal','2023-02-28',['common_perception_perception_objects_prod', 'common_perception_vision_road_detection'])
# my.query_history_record('ad1.4.1','normal','network',['sar_s1','eth0','tx','kB/s'],'2023-03-03')
# my.query_history_record('ad1.4.1','normal','power',[3],'2023-03-03')

# my.compare_date('ad1.4.1','normal',['common_perception_perception_objects_prod','common_perception_svc_perception_prod'])
