CREATE DATABASE `project_t03_platedection`;

CREATE TABLE `project_t03_platedetection`.`car_management` ( `id` INT(3) NOT NULL AUTO_INCREMENT , `car_plate` VARCHAR(255) NOT NULL , `enter_time` VARCHAR(255) NOT NULL , `car_place` VARCHAR(255) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

CREATE TABLE `project_t03_platedetection`.`place_management` ( `id` INT NOT NULL AUTO_INCREMENT , `car_plate` VARCHAR(255) NOT NULL , `isEmpty` BOOLEAN NOT NULL , `place_name` VARCHAR(255) NOT NULL , PRIMARY KEY (`id`), UNIQUE (`place_name`)) ENGINE = InnoDB;