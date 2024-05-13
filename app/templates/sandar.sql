-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 12, 2018 at 07:59 AM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sandar`
--

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `name`) VALUES
(1, 'Pagoda'),
(2, 'Hotel'),
(3, 'Restaurant'),
(4, 'Store and Shop'),
(5, 'Banks'),
(6, 'Cafe'),
(7, 'Junction'),
(8, 'Others');

-- --------------------------------------------------------

--
-- Table structure for table `links`
--

CREATE TABLE `links` (
  `id` int(11) NOT NULL,
  `node1` int(11) NOT NULL,
  `node2` int(11) NOT NULL,
  `distance` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `links`
--

INSERT INTO `links` (`id`, `node1`, `node2`, `distance`) VALUES
(1, 1, 2, 410),
(2, 1, 8, 1755),
(3, 2, 3, 455),
(4, 2, 7, 1490),
(5, 3, 4, 705),
(6, 4, 5, 616),
(7, 4, 6, 510),
(8, 5, 6, 395),
(9, 5, 10, 255),
(10, 6, 7, 290),
(11, 7, 8, 425),
(12, 7, 9, 322),
(13, 8, 9, 335),
(14, 8, 13, 482),
(15, 9, 12, 700),
(16, 9, 13, 388),
(17, 10, 11, 655),
(18, 11, 12, 503),
(19, 11, 16, 255),
(20, 12, 15, 251),
(21, 13, 14, 235),
(22, 14, 18, 668),
(23, 14, 21, 878),
(24, 15, 18, 201),
(25, 16, 17, 305),
(26, 17, 18, 643),
(27, 17, 20, 363),
(28, 18, 19, 220),
(29, 19, 20, 1080),
(30, 19, 21, 362),
(36, 20, 22, 543),
(37, 21, 22, 419),
(38, 23, 3, 200),
(39, 16, 15, 550);

-- --------------------------------------------------------

--
-- Table structure for table `places`
--

CREATE TABLE `places` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `cat_id` int(11) NOT NULL,
  `lat` double NOT NULL,
  `long` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `places`
--

INSERT INTO `places` (`id`, `name`, `cat_id`, `lat`, `long`) VALUES
(1, 'Kyakt Taung Pagoda', 1, 22.014296, 96.447091),
(2, 'Police Station', 8, 22.014722, 96.450895),
(3, 'Famous Hotel', 2, 22.012989, 96.454909),
(4, 'Lan San Aung Cafe', 6, 22.014854, 96.461379),
(5, 'Junction(Ztwda)', 7, 22.016014, 96.467126),
(6, 'Tai Puti Hotel (Daw Win)', 2, 22.01861, 96.464128),
(7, 'No 4 Quarter Office', 8, 22.02094, 96.46303),
(8, 'View Corner Restaurant', 3, 22.02394, 96.460295),
(9, 'Sitta ThuKa Medicine Store', 4, 22.023381, 96.463702),
(10, 'Htee Hlaing', 8, 22.016435, 96.469471),
(11, 'Sabdar May Food', 8, 22.021061, 96.473173),
(12, 'Nay La Thuka Hotel', 2, 22.023155, 96.468492),
(13, 'KBZ Bank', 5, 22.026884, 96.4641),
(14, 'Pin Se Cafe', 6, 22.028928, 96.465214),
(15, 'Shwe Si Gone Junction', 7, 22.024692, 96.470421),
(16, 'Mya NanTaw Hotel', 2, 22.022513, 96.474771),
(17, 'Su PaungRestaurant', 3, 22.024068, 96.476552),
(18, 'Shwe Kyal Store', 4, 22.026332, 96.470908),
(19, 'Toyota U Than Shwe (Shop)', 4, 22.028505, 96.471483),
(20, 'Sein Restaurant', 3, 22.028505, 96.47799),
(21, 'Sandar Book Store', 4, 22.031904, 96.472356),
(22, 'Shwe Moon Tyre Shop', 4, 22.032054, 96.476595),
(23, 'Wing 2', 8, 22.009387, 96.454647);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `links`
--
ALTER TABLE `links`
  ADD PRIMARY KEY (`id`),
  ADD KEY `node1` (`node1`),
  ADD KEY `node2` (`node2`);

--
-- Indexes for table `places`
--
ALTER TABLE `places`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cat_id` (`cat_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `links`
--
ALTER TABLE `links`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;
--
-- AUTO_INCREMENT for table `places`
--
ALTER TABLE `places`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `links`
--
ALTER TABLE `links`
  ADD CONSTRAINT `links_ibfk_1` FOREIGN KEY (`node1`) REFERENCES `places` (`id`),
  ADD CONSTRAINT `links_ibfk_2` FOREIGN KEY (`node2`) REFERENCES `places` (`id`);

--
-- Constraints for table `places`
--
ALTER TABLE `places`
  ADD CONSTRAINT `places_ibfk_1` FOREIGN KEY (`cat_id`) REFERENCES `categories` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
