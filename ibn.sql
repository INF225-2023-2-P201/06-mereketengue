-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-11-2023 a las 03:47:45
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ibn`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `firewall`
--

CREATE TABLE `firewall` (
  `ID` int(100) NOT NULL,
  `Interface` varchar(10) NOT NULL,
  `IPv4` varchar(18) NOT NULL,
  `Subnet Mask` varchar(18) NOT NULL,
  `Zona` varchar(18) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `firewall`
--

INSERT INTO `firewall` (`ID`, `Interface`, `IPv4`, `Subnet Mask`, `Zona`) VALUES
(1, 'Et0/0', '192.168.1.1', '255.255.255.0', 'inside'),
(2, 'Et0/1', '209.165.200.226', '255.255.255.252', 'outside'),
(3, 'Et0/2', '192.168.2.1', '255.255.255.0', 'dmz');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pc/server`
--

CREATE TABLE `pcserver` (
  `ID` int(100) NOT NULL,
  `Nombre` varchar(20) NOT NULL,
  `Interface` varchar(10) NOT NULL,
  `IPv4` varchar(18) NOT NULL,
  `Subnet Mask` varchar(18) NOT NULL,
  `Default Gateway` varchar(18) NOT NULL,
  `DNS Server` varchar(18) NOT NULL,
  `Zona` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pc/server`
--

INSERT INTO `pcserver` (`ID`, `Nombre`, `Interface`, `IPv4`, `Subnet Mask`, `Default Gateway`, `DNS Server`, `Zona`) VALUES
(1, 'server0', 'Fa0', '209.165.201.2', '255.255.255.0', '209.165.201.1', '209.165.201.2', 'outside'),
(2, 'pc3', 'Fa0', '192.168.1.10', '255.255.255.0', '192.168.1.1', '209.165.201.2', 'inside'),
(3, 'pc4', 'Fa0', '192.168.1.11', '255.255.255.0', '192.168.1.1', '209.165.201.2', 'inside'),
(4, 'pc2', 'Fa0', '192.168.2.10', '255.255.255.0', '192.168.2.1', '209.165.201.2', 'dmz'),
(5, 'pc1', 'Fa0', '192.168.2.11', '255.255.255.0', '192.168.2.1', '209.165.201.2', 'dmz');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `router`
--

CREATE TABLE `router` (
  `ID` int(100) NOT NULL,
  `Nombre` varchar(25) NOT NULL,
  `Interface` varchar(10) NOT NULL,
  `IPv4` varchar(18) NOT NULL,
  `Subnet Mask` varchar(18) NOT NULL,
  `Zona` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `router`
--

INSERT INTO `router` (`ID`, `Nombre`, `Interface`, `IPv4`, `Subnet Mask`, `Zona`) VALUES
(1, '', 'Gig0/0/0', '209.165.201.1', '255.255.255.0', 'outside'),
(1, '', 'Gig0/0/1', '209.165.200.225', '255.255.255.252', 'outside');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
