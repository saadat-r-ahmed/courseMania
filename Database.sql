-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 05, 2022 at 11:01 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cse370_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` varchar(12) NOT NULL,
  `name` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `name`, `email`, `password`) VALUES
('temp1', 'Saadat', 'blah1@gmail.com', '111'),
('temp2', 'Rafid', 'blah2@gmail.com', '222');

-- --------------------------------------------------------

--
-- Table structure for table `assesment`
--

CREATE TABLE `assesment` (
  `course` varchar(8) NOT NULL,
  `semester` varchar(12) NOT NULL,
  `type` varchar(20) NOT NULL,
  `deadline` date NOT NULL,
  `description` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `assesment`
--

INSERT INTO `assesment` (`course`, `semester`, `type`, `deadline`, `description`) VALUES
('CSE370', 'Fall2021', 'Assignment2', '2021-12-20', 'You have to do the task by midnight'),
('CSE370', 'Fall2021', 'Assignment3', '2020-01-08', 'The deadline is at 5 PM.  '),
('CSE370', 'Summer2021', 'Assignment4', '2022-01-01', 'SSS'),
('CSE370', 'Summer2021', 'Assignment5', '2020-01-23', 'The form is given here');

-- --------------------------------------------------------

--
-- Table structure for table `marks`
--

CREATE TABLE `marks` (
  `student_id` int(12) NOT NULL,
  `course` varchar(8) NOT NULL,
  `semester` varchar(12) NOT NULL,
  `type` varchar(20) NOT NULL,
  `total_marks` float(5,2) NOT NULL,
  `achieved_marks` float(5,2) NOT NULL,
  `updated_by` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `marks`
--

INSERT INTO `marks` (`student_id`, `course`, `semester`, `type`, `total_marks`, `achieved_marks`, `updated_by`) VALUES
(20101425, 'CSE370', 'Fall2021', 'Assignment2', 999.99, 999.99, 'SRA'),
(20101434, 'CSE370', 'Fall2021', 'Assignment3', 100.00, 100.00, 'SRA');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `student_id` int(12) NOT NULL,
  `name` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` varchar(60) NOT NULL,
  `administer` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`student_id`, `name`, `email`, `password`, `administer`) VALUES
(20101067, 'Mansur', 'stublah3@gmail.com', 'w13oihk', 'temp2'),
(20101425, 'Saadat Rafid Ahmed', 'stublah1@gmail.com', '111123asdfasdf', 'temp1'),
(20101434, 'Rubayet', 'stublah2@gmail.com', '1231234', 'temp1');

-- --------------------------------------------------------

--
-- Table structure for table `takes_in`
--

CREATE TABLE `takes_in` (
  `student_id` int(12) NOT NULL,
  `course` varchar(8) NOT NULL,
  `semester` varchar(12) NOT NULL,
  `type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `ta_modifies`
--

CREATE TABLE `ta_modifies` (
  `teacher_id` varchar(20) NOT NULL,
  `course` varchar(8) NOT NULL,
  `semester` varchar(12) NOT NULL,
  `type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ta_modifies`
--

INSERT INTO `ta_modifies` (`teacher_id`, `course`, `semester`, `type`) VALUES
('SRA', 'CSE370', 'Fall2021', 'Assignment2'),
('SRA', 'CSE370', 'Fall2021', 'Assignment3'),
('SRA', 'CSE370', 'Summer2021', 'Assignment4'),
('SRA', 'CSE370', 'Summer2021', 'Assignment5');

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `teacher_id` varchar(20) NOT NULL,
  `name` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` varchar(60) NOT NULL,
  `appointed_by` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`teacher_id`, `name`, `email`, `password`, `appointed_by`) VALUES
('SRA', 'Saadat Rafid Ahmed', 'sad@gmail.com', '111', 'temp1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `assesment`
--
ALTER TABLE `assesment`
  ADD PRIMARY KEY (`course`,`semester`,`type`);

--
-- Indexes for table `marks`
--
ALTER TABLE `marks`
  ADD PRIMARY KEY (`student_id`,`course`,`semester`,`type`),
  ADD KEY `marks_ibfk_1` (`course`,`semester`,`type`),
  ADD KEY `marks_ibfk_3` (`updated_by`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`),
  ADD KEY `administer` (`administer`);

--
-- Indexes for table `takes_in`
--
ALTER TABLE `takes_in`
  ADD PRIMARY KEY (`student_id`,`course`,`semester`,`type`),
  ADD KEY `student_id` (`student_id`,`course`,`semester`,`type`),
  ADD KEY `takes_in_ibfk_1` (`course`,`semester`,`type`);

--
-- Indexes for table `ta_modifies`
--
ALTER TABLE `ta_modifies`
  ADD PRIMARY KEY (`teacher_id`,`course`,`semester`,`type`),
  ADD KEY `ta_modifies_ibfk_1` (`course`,`semester`,`type`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`teacher_id`),
  ADD KEY `appointed_by` (`appointed_by`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `marks`
--
ALTER TABLE `marks`
  ADD CONSTRAINT `marks_ibfk_1` FOREIGN KEY (`course`,`semester`,`type`) REFERENCES `assesment` (`course`, `semester`, `type`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `marks_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `marks_ibfk_3` FOREIGN KEY (`updated_by`) REFERENCES `teacher` (`teacher_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`administer`) REFERENCES `admin` (`id`) ON UPDATE CASCADE;

--
-- Constraints for table `takes_in`
--
ALTER TABLE `takes_in`
  ADD CONSTRAINT `takes_in_ibfk_1` FOREIGN KEY (`course`,`semester`,`type`) REFERENCES `assesment` (`course`, `semester`, `type`) ON UPDATE CASCADE,
  ADD CONSTRAINT `takes_in_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`);

--
-- Constraints for table `ta_modifies`
--
ALTER TABLE `ta_modifies`
  ADD CONSTRAINT `ta_modifies_ibfk_1` FOREIGN KEY (`course`,`semester`,`type`) REFERENCES `assesment` (`course`, `semester`, `type`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ta_modifies_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `teacher`
--
ALTER TABLE `teacher`
  ADD CONSTRAINT `teacher_ibfk_1` FOREIGN KEY (`appointed_by`) REFERENCES `admin` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
