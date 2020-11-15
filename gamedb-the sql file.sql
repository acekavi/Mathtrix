-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 09, 2020 at 11:28 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gamedb`
--

-- --------------------------------------------------------

--
-- Table structure for table `easy`
--

CREATE TABLE `easy` (
  `gameID` varchar(4) NOT NULL,
  `Player` varchar(255) NOT NULL,
  `Questions` int(2) NOT NULL,
  `Highscore` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `easy`
--

INSERT INTO `easy` (`gameID`, `Player`, `Questions`, `Highscore`) VALUES
('E10', 'Kamal', 5, 100),
('E11', 'Namal', 5, 40),
('E14', 'Heath', 5, 100),
('E15', 'Kavinda', 5, 100),
('E17', 'Avishka', 7, 100),
('E3', 'Ace', 5, 100),
('E6', 'Saman', 5, 80),
('E7', 'Zhagy', 5, 100);

-- --------------------------------------------------------

--
-- Table structure for table `hard`
--

CREATE TABLE `hard` (
  `gameID` varchar(4) NOT NULL,
  `Player` varchar(255) NOT NULL,
  `Questions` int(2) NOT NULL,
  `Highscore` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hard`
--

INSERT INTO `hard` (`gameID`, `Player`, `Questions`, `Highscore`) VALUES
('H1', 'Avishka', 5, 100);

-- --------------------------------------------------------

--
-- Table structure for table `medium`
--

CREATE TABLE `medium` (
  `gameID` varchar(4) NOT NULL,
  `Player` varchar(255) NOT NULL,
  `Questions` int(2) NOT NULL,
  `Highscore` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `medium`
--

INSERT INTO `medium` (`gameID`, `Player`, `Questions`, `Highscore`) VALUES
('M1', 'Avishka', 5, 100),
('M2', 'Ace', 7, 100),
('M3', 'Joker', 3, 100),
('M4', 'Kavinda', 3, 67);

-- --------------------------------------------------------

--
-- Table structure for table `misc`
--

CREATE TABLE `misc` (
  `miscID` int(11) NOT NULL,
  `mode` varchar(1) NOT NULL,
  `inc` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `misc`
--

INSERT INTO `misc` (`miscID`, `mode`, `inc`) VALUES
(1, 'E', 19),
(2, 'M', 5),
(3, 'H', 4),
(4, 'T', 25);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `easy`
--
ALTER TABLE `easy`
  ADD PRIMARY KEY (`gameID`);

--
-- Indexes for table `hard`
--
ALTER TABLE `hard`
  ADD PRIMARY KEY (`gameID`);

--
-- Indexes for table `medium`
--
ALTER TABLE `medium`
  ADD PRIMARY KEY (`gameID`);

--
-- Indexes for table `misc`
--
ALTER TABLE `misc`
  ADD PRIMARY KEY (`miscID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `misc`
--
ALTER TABLE `misc`
  MODIFY `miscID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
