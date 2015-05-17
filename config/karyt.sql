
DROP TABLE IF EXISTS `aliases`;

CREATE TABLE `aliases` (
  `alias` varchar(256) NOT NULL,
  `pubkey` varchar(256) NOT NULL,
  `created` datetime NOT NULL,
  `confirmed` tinyint DEFAULT 0,
  `ip` varchar(16) DEFAULT NULL,
  `confirmkey` varchar(64) NOT NULL,
  UNIQUE KEY `aliases_alias` (`alias`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
