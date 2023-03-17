CREATE TABLE `case_table` (
  `id` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `region` varchar(255) NOT NULL,
  `version` varchar(255) NOT NULL,
  `scene` varchar(255) NOT NULL,
  `taskid` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `perception_framerate` (
  `ID` varchar(255) NOT NULL,
  `common_perception_perception_objects_prod` float,
  `common_perception_vision_road_detection` float,
  `common_perception_vision_feature_flag_prod` float,
  `common_perception_vision_perception_objects_prod` float,
  `common_perception_od_output_adb` float,
  `common_perception_od_output_adp` float,
  `common_perception_od_output_prod` float,
  `common_perception_od_output_lidar_prod` float,
  `common_perception_svc_perception_prod` float,
  `common_perception_svc_nn_output` float,
  `coapp_common_perception_perception_objects` float,
  `coapp_common_perception_vision_road_detection` float,
  `coapp_common_perception_od_output` float,
  PRIMARY KEY (`ID`),
    CONSTRAINT `fk_framerate_case_id` FOREIGN KEY (`id`) REFERENCES `case_table` (`id`) ON DELETE CASCADE ON UPDATE CASCADE

);

CREATE TABLE power (
  `id` varchar(255) NOT NULL,
  `core` int NOT NULL,
  `main_power` float NOT NULL,
  `secondary_power` float NOT NULL,
  PRIMARY KEY (`id`,`core`),
  CONSTRAINT `fk_power_case_id` FOREIGN KEY (`id`) REFERENCES `case_table` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE app_thread (
    `id` varchar(255) NOT NULL,
    `core` int NOT NULL,
    `service` VARCHAR(255) NOT NULL,
    `module_name` VARCHAR(255) NOT NULL,
    `category` VARCHAR(255) NOT NULL,
    `thd_num` INT NOT NULL,
    `min` FLOAT NOT NULL,
    `mean` FLOAT NOT NULL,
    `max` FLOAT NOT NULL,
    PRIMARY KEY (`id`, `core`, `service`, `module_name`, `category`),
  CONSTRAINT `fk_app_case_id` FOREIGN KEY (`id`) REFERENCES `case_table` (`id`) ON DELETE CASCADE ON UPDATE CASCADE

);

CREATE TABLE app_proc (
  `id` varchar(255) NOT NULL,
  `core` INT NOT NULL,
  `app_name` VARCHAR(255) NOT NULL,
  `cpumem` VARCHAR(255) NOT NULL,
  `mean` FLOAT NOT NULL,
  `max` FLOAT NOT NULL,
  PRIMARY KEY(`id`,`core`,`app_name`,`cpumem`),
  CONSTRAINT `fk_proc_case_id` FOREIGN KEY (`id`) REFERENCES `case_table` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE cpu_mem (
  `id` varchar(255) NOT NULL,
  `core` INT NOT NULL,
  `category` VARCHAR(255),
  `mean` FLOAT NOT NULL,
  `max` FLOAT NOT NULL,
  PRIMARY KEY(`id`,`core`,`category`),
  CONSTRAINT `fk_cpu_case_id` FOREIGN KEY (`id`) REFERENCES `case_table` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `network` (
  `id` varchar(255) NOT NULL,
  `core` varchar(255) NOT NULL,
  `metric` varchar(255) NOT NULL,
  `txrx` varchar(255) NOT NULL,
  `kbpck` varchar(255) NOT NULL,
  `mean` float NOT NULL,
  `max` float NOT NULL,
  PRIMARY KEY (`id`,`core`,`app`,`txrx`,`kbpck`),
  CONSTRAINT `fk_net_case_id` FOREIGN KEY (`id`) REFERENCES `case_table` (`id`) ON DELETE CASCADE ON UPDATE CASCADE

);


SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE case;
SET FOREIGN_KEY_CHECKS = 1;

SELECT 
    c.version,
    p.common_perception_perception_objects_prod
FROM 
    case_table c
    INNER JOIN perception_framerate p ON c.id = p.ID
WHERE 
    c.date = '2023-02-28'
    AND c.scene = 'normal'
    AND c.version IN ('master', 'ad1.4.1')
ORDER BY 
    c.version ASC;

"SELECT pf.ID, ct.version, pf.common_perception_perception_objects_prod, pf.common_perception_vision_road_detection FROM perception_framerate pf JOIN case_table ct ON pf.ID = ct.id WHERE ct.version IN ('master', 'ad1.4.1') AND ct.scene = 'normal' AND ct.date = '2023-03-03'"   

SELECT c.id,common_perception_perception_objects_prod FROM perception_framerate 
                    JOIN case_table c ON perception_framerate.ID = c.id 
                    WHERE c.version = 'ad1.4.1' AND c.scene = 'normal' 
                    AND DATE(c.date) = DATE('2023-03-03') 

SELECT date, version, region, scene,  core, category, mean, max FROM cpu_mem JOIN case_table c ON cpu_mem.ID = c.id WHERE c.version = IN ('master') AND c.scene IN ('parking') AND DATE(c.date) in ('2023-02-28','2023-02-27','2023-02-26') AND core = 2 AND category = 'cpu';

SELECT * FROM cpu_mem WHERE id = %s AND core=%s AND app_name = `%s` AND cpumem=%s

SELECT v1.main_power, v2.main_power, v1.secondary_power, v2.secondary_power,c1.id
FROM power v1
INNER JOIN power v2 ON v1.id = v2.id AND v1.core = v2.core
 JOIN case_table c1 ON v1.id = c1.id
JOIN case_table c2 ON v2.id = c2.id
WHERE c1.version = 'master_CN' AND c2.version = 'ad1.4.1_CN';