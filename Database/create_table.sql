# logou_job
DROP TABLE IF EXISTS lagou_job;
CREATE TABLE lagou_job
(
	id int UNSIGNED auto_increment,
	positionId VARCHAR(255) DEFAULT NULL,
	positionName VARCHAR(255) DEFAULT NULL,
	companyId VARCHAR(255) DEFAULT NULL,
	companyFullName VARCHAR(255) DEFAULT NULL,
	companyShortName VARCHAR(255) DEFAULT NULL,
	companySize VARCHAR(255) DEFAULT NULL,
	industryField VARCHAR(255) DEFAULT NULL,
	financeStage VARCHAR(255) DEFAULT NULL,
	companyLabelList VARCHAR(255) DEFAULT NULL,
	firstType VARCHAR(255) DEFAULT NULL,
	secondType VARCHAR(255) DEFAULT NULL,
	thirdType VARCHAR(255) DEFAULT NULL,
	skillLables VARCHAR(255) DEFAULT NULL,
	positionLables VARCHAR(255) DEFAULT NULL,
	industryLables VARCHAR(255) DEFAULT NULL,
	creatTime VARCHAR(255) DEFAULT NULL,
	city VARCHAR(255) DEFAULT NULL,
	district VARCHAR(255) DEFAULT NULL,
	salary VARCHAR(255) DEFAULT NULL,
	salaryMonth VARCHAR(255) DEFAULT NULL,
	workYear VARCHAR(255) DEFAULT NULL,
	jobNature VARCHAR(255) DEFAULT NULL,
	education VARCHAR(255) DEFAULT NULL,
	positionAdvantage VARCHAR(255) DEFAULT NULL,
	subwayline VARCHAR(255) DEFAULT NULL,
	stationname VARCHAR(255) DEFAULT NULL,
	linestaion VARCHAR(255) DEFAULT NULL,
	isSchoolJob VARCHAR(255) DEFAULT NULL,
	jobAdvantage VARCHAR(255) DEFAULT NULL,
	jobDescription VARCHAR(255) DEFAULT NULL,
	workAddr VARCHAR(255) DEFAULT NULL,
	keyWord VARCHAR(255) DEFAULT NULL,
	dataDate VARCHAR(255) DEFAULT NULL,
	
	PRIMARY KEY (id)
	
);


COMMIT;

