DROP TABLE IF EXISTS lagou_job_clean;
CREATE TABLE lagou_job_clean LIKE lagou_job;
INSERT INTO lagou_job_clean SELECT * FROM lagou_job;
	

# createTime
UPDATE lagou_job_clean SET createTime = SUBSTRING_INDEX(createTime,'.',1);

# publishTime
UPDATE lagou_job_clean SET publishTime = REPLACE(publishTime,'发布','');
UPDATE lagou_job_clean SET publishTime = CONCAT(DATE(createTime),' ',publishTime, ':00') WHERE publishTime LIKE '%:%';
UPDATE lagou_job_clean SET publishTime = DATE_SUB(createTime,INTERVAL LEFT(publishTime,1) DAY) WHERE publishTime LIKE '%天前';
UPDATE lagou_job_clean SET publishTime = CONCAT(publishTime,' ','00:00:00') WHERE publishTime NOT LIKE '%:%';

# jobAddr
UPDATE lagou_job_clean SET jobAddr = REPLACE(REPLACE(REPLACE(jobAddr,'\n',''),' ',''),'查看地图','');

# jobDetail
UPDATE lagou_job_clean SET jobDetail = TRIM('\n' FROM jobDetail);

DROP TABLE IF EXISTS z_newcreate_tmp;
CREATE TABLE z_newcreate_tmp LIKE lagou_job_clean;
INSERT INTO z_newcreate_tmp(positionId,salary,companyName,positionName,companyId,positionLink,district,publishTime,workYear,education,industry,skillLables,companyLabeles,jobDetail,jobAddr,keyWord,createTime)
	SELECT positionId,salary,companyName,positionName,companyId,positionLink,district,publishTime,workYear,education,industry,skillLables,companyLabeles,jobDetail,jobAddr,keyWord,createTime FROM lagou_job_clean ORDER BY publishTime DESC;
TRUNCATE TABLE lagou_job_clean;
INSERT INTO lagou_job_clean
	SELECT * FROM z_newcreate_tmp WHERE id IN(SELECT MIN(id) FROM z_newcreate_tmp GROUP BY positionId);


DROP TABLE IF EXISTS lagou_job_new;
CREATE TABLE lagou_job_new 
	SELECT positionName, salary, skillLables, companyName, companyLabeles, jobDetail, jobAddr, positionLink FROM lagou_job_clean WHERE positionId NOT IN(SELECT positionId FROM lagou_job_history);

INSERT INTO lagou_job_history(positionId,salary,companyName,positionName,companyId,positionLink,district,publishTime,workYear,education,industry,skillLables,companyLabeles,jobDetail,jobAddr,keyWord,createTime)
	SELECT positionId,salary,companyName,positionName,companyId,positionLink,district,publishTime,workYear,education,industry,skillLables,companyLabeles,jobDetail,jobAddr,keyWord,createTime FROM lagou_job_clean;
TRUNCATE TABLE lagou_job;

COMMIT;

	