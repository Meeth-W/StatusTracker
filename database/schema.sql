-- Users Tracked
CREATE TABLE IF NOT EXISTS `track` (
  `user_id` varchar(20) PRIMARY KEY,
  `reqestor_id` varchar(20) NOT NULL,
  `tracking_since` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Blacklist
CREATE TABLE IF NOT EXISTS `blacklist` (
    `id` int(11) NOT NULL,
    `user_id` varchar(20) NOT NULL,
    `reason` varchar(255) NOT NULL,
    `server_id` varchar(20) NOT NULL,
    `moderator_id` varchar(20) NOT NULL
);

-- Admin Users
CREATE TABLE IF NOT EXISTS `admins` (
    `user_id` varchar(20) PRIMARY KEY,
    `permissions` varchar(15) NOT NULL DEFAULT `helper`
);