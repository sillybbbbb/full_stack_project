import mysql.connector
import json
from util import *
from prettytable import PrettyTable
import datetime
class MyDatabase:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def connect(self):
        self.cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
        
    def disconnect(self):
        self.cnx.close()
    def add_to_case(self, id,date, region, version_name, scene, taskid):
      
        self.cursor = self.cnx.cursor()
            # 首先查询是否存在相同的记录
        sql = "SELECT * FROM case_table WHERE id=%s"
        self.cursor.execute(sql, ([id]))
        result = self.cursor.fetchone()
        if result is None:

        # 插入值的 SQL 语句
            add_case = "INSERT INTO `case_table` (id,date, region, version, scene, taskid) VALUES (%s,%s, %s, %s, %s, %s)"

            # 值的元组
            case_data = (id, date, region, version_name, scene, taskid)

        # 执行插入操作
        #INSERT INTO `case` (id,date, region, version, scene, taskid) VALUES ('20230228_63fcfd6621e32159b2fbe3f9_normal','2023-02-28','CN','master','normal','63fcfd6621e32159b2fbe3f9')
        # cursor = self.cnx.cursor()
        # print(add_case)
            self.cursor.execute(add_case, case_data)
            self.cnx.commit()
            print("添加case成功")
        else:
            print("已存在")

        


# 向 perception_framerate 表中插入数据
    def add_to_perception_framerate(self, id_val, perception_objects, vision_road_detection, vision_feature_flag, perception_objects_2, od_output_adb, od_output_adp, od_output, od_output_lidar, svc_perception, svc_nn_output, perception_objects_coapp, vision_road_detection_coapp, od_output_coapp):
        """
        将感知帧率数据插入到perception_framerate表中
        """

        try:
            self.cursor = self.cnx.cursor()
            
            # 首先查询是否存在相同的记录
            sql = "SELECT * FROM perception_framerate WHERE id=%s"
            self.cursor.execute(sql, (id_val,))
            result = self.cursor.fetchone()
            
            if result is None:
                # 如果不存在相同的记录，则插入新记录
                sql = "INSERT INTO perception_framerate (id, common_perception_perception_objects_prod, common_perception_vision_road_detection, common_perception_vision_feature_flag_prod, common_perception_vision_perception_objects_prod, common_perception_od_output_adb, common_perception_od_output_adp, common_perception_od_output_prod, common_perception_od_output_lidar_prod, common_perception_svc_perception_prod, common_perception_svc_nn_output, coapp_common_perception_perception_objects, coapp_common_perception_vision_road_detection, coapp_common_perception_od_output) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                self.cursor.execute(sql, (id_val, perception_objects, vision_road_detection, vision_feature_flag, perception_objects_2, od_output_adb, od_output_adp, od_output, od_output_lidar, svc_perception, svc_nn_output, perception_objects_coapp, vision_road_detection_coapp, od_output_coapp))
                self.cnx.commit()
                print("添加感知帧率数据成功")
            else:
                # 如果存在相同的记录，则更新已有记录
                sql = "UPDATE perception_framerate SET common_perception_perception_objects_prod=%s, common_perception_vision_road_detection=%s, common_perception_vision_feature_flag_prod=%s, common_perception_vision_perception_objects_prod=%s, common_perception_od_output_adb=%s, common_perception_od_output_adp=%s, common_perception_od_output_prod=%s, common_perception_od_output_lidar_prod=%s, common_perception_svc_perception_prod=%s, common_perception_svc_nn_output=%s, coapp_common_perception_perception_objects=%s, coapp_common_perception_vision_road_detection=%s, coapp_common_perception_od_output=%s WHERE id=%s"
                self.cursor.execute(sql, (perception_objects, vision_road_detection, vision_feature_flag, perception_objects_2, od_output_adb, od_output_adp, od_output, od_output_lidar, svc_perception, svc_nn_output, perception_objects_coapp, vision_road_detection_coapp, od_output_coapp,id_val))
                self.cnx.commit()
                print("更新感知帧率数据成功")
        except Exception as e:
            self.cnx.rollback()
            print("添加感知帧率数据失败：", e)
        

# 向 power 表中插入数据
    def add_to_power(self, id_val, core, main,second):
        """
        将功耗数据插入到power表中
        """
        try:
            self.cursor = self.cnx.cursor()

            # 首先查询是否存在相同的记录
            sql = "SELECT * FROM power WHERE id=%s and core=%s"
            self.cursor.execute(sql, (id_val,core))
            result = self.cursor.fetchone()
            
            if result is None:
                # 如果不存在相同的记录，则插入新记录
                sql = "INSERT INTO power (id, core, main_power,secondary_power) VALUES (%s, %s, %s, %s)"
                self.cursor.execute(sql, (id_val, core, main,second))
                self.cnx.commit()
                print("添加功耗数据成功")
            else:
                # 如果存在相同的记录，则更新已有记录
                sql = "UPDATE power SET core=%s, main_power=%s,secondary_power=%s WHERE id=%s"
                self.cursor.execute(sql, (core, main,second, id_val))
                self.cnx.commit()
                print("更新功耗数据成功")
        except Exception as e:
            self.cnx.rollback()
            print("添加/更新功耗数据失败：", e)

    def add_to_app(self, id,core, service, module_name, category, thd_num, min_val, mean_val, max_val):
        """
        将应用程序性能数据插入到app表中
        """
        try:
            self.cursor = self.cnx.cursor()

            # 首先查询是否存在相同的记录- 
            sql = "SELECT * FROM app WHERE id = %s AND core=%s AND service=%s AND module_name=%s AND category=%s"
            self.cursor.execute(sql, (id,core, service, module_name, category))
            result = self.cursor.fetchone()
            
            if result is None:
                # 如果不存在相同的记录，则插入新记录
                sql = "INSERT INTO app (id,core, service, module_name, category, thd_num, min, mean, max) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)"
                self.cursor.execute(sql, (id,core, service, module_name, category, thd_num, min_val, mean_val, max_val))
                self.cnx.commit()
                print("添加应用程序性能数据成功")
            else:
                # 如果存在相同的记录，则更新已有记录
                sql = "UPDATE app SET thd_num=%s, min=%s, mean=%s, max=%s WHERE id = %s AND core=%s AND service=%s AND module_name=%s AND category=%s"
                self.cursor.execute(sql, (thd_num, min_val, mean_val, max_val, id,core, service, module_name, category))
                self.cnx.commit()
                print("更新应用程序性能数据成功")
        except Exception as e:
            self.cnx.rollback()
            print("添加应用程序性能数据失败：", e)

    def add_to_proc(self,id,core,app,cpumem,mean,max):
        try:
            self.cursor = self.cnx.cursor()

            # 首先查询是否存在相同的记录- 
            sql = "SELECT * FROM app_proc WHERE id = %s AND core=%s AND app_name = %s AND cpumem=%s"
            self.cursor.execute(sql, (id,core,app, cpumem))
            result = self.cursor.fetchone()
            if result is None:
                sql = "INSERT INTO app_proc (id, core, app_name,cpumem,mean,max) VALUES (%s,%s, %s, %s,%s,%s)"
                self.cursor.execute(sql, (id,core, app,cpumem,mean,max))
                self.cnx.commit()
                print("添加APP_PROC性能数据成功")
    # Execute the SQL query with the given parameter values
            else:
                sql = "UPDATE app_proc SET mean =%s AND max = %s WHERE id = %s AND core=%s AND app_name =%s AND cpumem=%s "
                self.cursor.execute(sql, (id,core, app,cpumem, mean,max))
                self.cnx.commit()
                print("更新APP_PROC性能数据成功")
        except Exception as e:
            self.cnx.rollback()
            print("添加APP_PROC性能数据失败：", e)

    def add_to_cpu(self,id,core,category,mean,max):
        try:
            self.cursor = self.cnx.cursor()

            # 首先查询是否存在相同的记录- 
            sql = "SELECT * FROM cpu_mem WHERE id = %s AND core=%s AND category=%s"
            self.cursor.execute(sql, (id,core, category))
            result = self.cursor.fetchone()
            if result is None:
                sql = "INSERT INTO cpu_mem (id, core, category,mean,max) VALUES (%s, %s, %s,%s,%s)"
                self.cursor.execute(sql, (id,core, category,mean,max))
                self.cnx.commit()
                print("添加CPU_MEM性能数据成功")
    # Execute the SQL query with the given parameter values
            else:
                sql = "UPDATE cpu_mem SET mean =%s AND max = %s WHERE id = %s AND core=%s AND category=%s "
                self.cursor.execute(sql, (id,core, category, mean,max))
                self.cnx.commit()
                print("更新CPU_MEM性能数据成功")
        except Exception as e:
            self.cnx.rollback()
            print("添加CPU_MEM性能数据失败：", e)
    
    def add_to_network(self, id, core, app, txrx, kbpck, mean, max):
        try:
            self.cursor = self.cnx.cursor()

            # 首先查询是否存在相同的记录
            sql = "SELECT * FROM network WHERE id = %s AND core=%s AND metric=%s AND txrx=%s AND kbpck=%s"
            self.cursor.execute(sql, (id, core, app, txrx, kbpck))
            result = self.cursor.fetchone()
            if result is None:
                sql = "INSERT INTO network (id, core, metric,  txrx, kbpck, mean, max) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                self.cursor.execute(sql, (id, core, app,  txrx, kbpck, mean, max))
                self.cnx.commit()
                print("添加网络性能数据成功")
            else:
                sql = "UPDATE network SET mean = %s, max = %s WHERE id = %s AND core = %s AND metric = %s AND  txrx = %s AND kbpck = %s"
                self.cursor.execute(sql, (mean, max, id, core, app, txrx, kbpck))
                self.cnx.commit()
                print("更新网络性能数据成功")
        except Exception as e:
            self.cnx.rollback()
            print("添加网络性能数据失败：", e)


    def PrettyPrint(self):
        results = self.cursor.fetchall()

        table = PrettyTable()
        header = [i[0] for i in self.cursor.description]
        table.field_names =  header

        for row in results:
            table.add_row(row)
        print(table)
        return results,header



    def query_version_compare(self, versions, scene, date, values):
        try:
            self.cursor = self.cnx.cursor()

            # 构造查询语句
            sql = f"SELECT ct.date, ct.version, ct.region,ct.scene"
            for val in values:
                sql += f", pf.{val}"
            sql += f" FROM perception_framerate pf JOIN case_table ct ON pf.ID = ct.id WHERE ct.version IN ({','.join(['%s']*len(versions))}) AND ct.scene = %s AND ct.date = %s"

            # 构造查询参数
            params = tuple(versions) + (scene, date)

            # 执行查询语句
            self.cursor.execute(sql, params)

            # 输出查询结果
            self.PrettyPrint()
            self.cursor.close()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
    def compare_date(self,version, scene,values):

        # value_str = ', '.join(values)
        try:
            self.cursor = self.cnx.cursor()

            # 查询语句，连接case_table和perception_framerate表，同时根据输入条件筛选数据
            sql = "SELECT date,ct.version, ct.region,ct.scene"
            for val in values:
                sql += f", pf.{val}"
            sql += f" FROM perception_framerate pf JOIN case_table ct ON pf.ID = ct.id WHERE ct.version = '{version}' AND ct.scene = '{scene}'"

            # 执行查询语句
            self.cursor.execute(sql)

            self.PrettyPrint()
            self.cursor.close()

                
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def query_history_record(self,version, scene, classes,metric, date):
        try:
            

            # 输入参数检查
            if not isinstance(version, str):
                raise ValueError("版本号应该为字符串类型")
            if not isinstance(scene, str):
                raise ValueError("场景应该为字符串类型")
            
            date = datetime.datetime.strptime(date, "%Y-%m-%d")


            # 执行SQL语句
            self.cursor = self.cnx.cursor()

            query = ("SELECT date, version, region, scene, {} FROM {} "
                    "JOIN case_table c ON {}.ID = c.id "
                    "WHERE c.version = %s AND c.scene = %s "
                    "AND DATE(c.date) = DATE(%s)")
            # header = ','.join(metric)
            if classes == 'perception_framerate':
                header = 'mean, max'
            elif classes == 'cpu_mem':
                # tmp_list = metric.split('_')
                core = metric[1]
                category = metric[0]
                query+= f" AND core = {core} AND category = '{category}'"
                header = ' core, category, mean, max'
            elif classes == 'network':
                # tmp_list = metric.split('-')
                core = metric[0]
                
                app = metric[1]
                txrx = metric[2]
                kb = metric[3]
                query+= f" AND core = '{core}' AND app = '{app}' AND txrx = '{txrx}' AND kbpck = '{kb}'"
                header = 'core, app, txrx, kbpck, mean, max'
            elif classes == 'app':#s3_service_Other_lidar_ctrl_max
                
                core = metric[0]
                service = metric[1]
                module_name = metric[2]
                category = metric[3]
       
                query+= f"  AND core = {core} AND service = '{service}' AND module_name = '{module_name}' AND category = '{category}'"
                header = ' core, service, module_name, category , mean, max'
            elif classes == 'power':
                core = metric[0]
                
                query+= f" AND core = {core} "
                header = ' core,  main_power, secondary_power'

            self.cursor.execute(query.format(header, classes,classes), (version, scene, date))
            # results =  cursor.fetchall()
            # header = [i[0] for i in self.cursor.description]
            results,col_name  = self.PrettyPrint()
            self.cursor.close()
            return results,col_name


        except mysql.connector.Error as err:
            print("数据库错误: {}".format(err))

        except ValueError as err:
            print("输入参数错误: {}".format(err))

        except Exception as err:
            print("其他错误: {}".format(err))
    

    def query_record(self,versions, scenes, metric, start,end):
        try:
            
            classes = metric[0]
            # # 输入参数检查
            # if not isinstance(version, str):
            #     raise ValueError("版本号应该为字符串类型")
            # if not isinstance(scene, str):
            #     raise ValueError("场景应该为字符串类型")
            
            # date = datetime.datetime.strptime(date, "%Y-%m-%d")


            # 执行SQL语句
            self.cursor = self.cnx.cursor()
            query = ("SELECT date, version, scene, {} FROM {} "
                "JOIN case_table c ON {}.ID = c.id "
                f"WHERE c.version IN ({','.join(['%s']*len(versions))}) AND c.scene IN ({','.join(['%s']*len(scenes))}) "
                "AND DATE(c.date) BETWEEN %s AND %s")
            # query = ("SELECT date, version, scene, {} FROM {} "
            #         "JOIN case_table c ON {}.ID = c.id "
            #         f"WHERE c.version IN ({','.join(['%s']*len(versions))}) AND c.scene IN ({','.join(['%s']*len(scenes))}) "
            #         f"AND DATE(c.date) in ({','.join(['%s']*len(date))})")
            # header = ','.join(metric)
            if classes == 'perception_framerate':
                header = metric[1]
            elif classes == 'cpu_mem':
                # tmp_list = metric.split('_')
                core = metric[1]
                category = metric[2]
                query+= f" AND core = {core} AND category = '{category}'"
                header = ' core as SOC, category, mean, max'
            elif classes == 'network':
                # tmp_list = metric.split('-')
                core ="sar_s" + str(metric[1])
                
                app = metric[2]
                # txrx = metric[2]
                # kb = metric[3]
                query+= f" AND core = '{core}' AND metric = '{app}'"
                
                # query+= f" AND core = '{core}' AND app = '{app}' AND txrx = '{txrx}' AND kbpck = '{kb}'"
                header = 'core as SOC, metric, txrx, kbpck, mean, max'
            elif classes == 'app':#s3_service_Other_lidar_ctrl_max
                
                core = metric[0]
                service = metric[1]
                module_name = metric[2]
                category = metric[3]
       
                query+= f"  AND core = {core} AND service = '{service}' AND module_name = '{module_name}' AND category = '{category}'"
                header = ' core as SOC, service, module_name, category , mean, max'
            elif classes == 'app_proc':#s3_service_Other_lidar_ctrl_max
                
                core = metric[1]
                
                app_name = metric[2]
                category = metric[3]
       
                query+= f"  AND core = {core} AND app_name = '{app_name}' AND cpumem = '{category}'"
                header = ' core as SOC, app_name, cpumem as `cpu/mem`, mean, max'

            elif classes == 'power':
                core = metric[1]
                
                query+= f" AND core = {core} "
                header = ' core as SOC,  main_power, secondary_power'
            print(query.format(header, classes,classes))
            self.cursor.execute(query.format(header, classes,classes), (tuple(versions)+tuple(scenes)+(start,end)))
            # results =  cursor.fetchall()
            # header = [i[0] for i in self.cursor.description]
            results,col_name  = self.PrettyPrint()
            res_js = []
            for res in results:
                d ={}
                for i in range(len(res)):
                    if(col_name[i] == 'date'):
                        d[col_name[i]] = res[i].strftime('%Y-%m-%d')
                        # print(res[i].strftime('%Y-%m-%d'))
                    else:
                        d[col_name[i]] = res[i]
                res_js.append(d)
            self.cursor.close()
            return res_js,col_name



        except mysql.connector.Error as err:
            print("数据库错误: {}".format(err))

        except ValueError as err:
            print("输入参数错误: {}".format(err))

        except Exception as err:
            print("其他错误: {}".format(err))
    

