use stars;

CREATE TABLE IF NOT EXISTS constellation(
	`id_constellation` int primary key auto_increment,
    `name_constellation` varchar(40));

CREATE TABLE IF NOT EXISTS stars(
	`id_star` int primary key auto_increment,
	`name` varchar(50),
    `brightness` float,
    `timestamp` datetime,
    `id_constellation` int,
    FOREIGN KEY(`id_constellation`) REFERENCES constellation(`id_constellation`));


