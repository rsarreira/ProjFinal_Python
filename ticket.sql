-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 05-Maio-2024 às 12:52
-- Versão do servidor: 10.4.32-MariaDB
-- versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `ticket2help`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `ticket`
--

CREATE TABLE `ticket` (
  `idTicket` int(10) NOT NULL,
  `idColab` int(10) NOT NULL,
  `datahoraGerado` datetime NOT NULL,
  `datahoraAtendido` datetime DEFAULT NULL,
  `datahoraResolvido` datetime DEFAULT NULL,
  `estadoTicket` varchar(20) NOT NULL,
  `estadoAtendimento` varchar(20) DEFAULT NULL,
  `tipoTicket` varchar(2) NOT NULL,
  `equipamento` varchar(50) DEFAULT NULL,
  `avaria` varchar(50) DEFAULT NULL,
  `software` varchar(50) DEFAULT NULL,
  `necessidade` varchar(50) DEFAULT NULL,
  `descRep` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `ticket`
--

INSERT INTO `ticket` (`idTicket`, `idColab`, `datahoraGerado`, `datahoraAtendido`, `datahoraResolvido`, `estadoTicket`, `estadoAtendimento`, `tipoTicket`, `equipamento`, `avaria`, `software`, `necessidade`, `descRep`) VALUES
(4, 1761, '2024-05-01 21:16:00', '2024-05-04 17:56:50', '2024-05-04 17:58:44', 'Atendido', 'Não resolvido', 'HW', 'rato', 'morreu', NULL, NULL, 'morto'),
(5, 1761, '2024-05-01 21:18:00', '2024-05-04 18:05:13', '2024-05-04 18:05:25', 'Atendido', 'Não resolvido', 'HW', 'rato', 'morreu', 'windows', 'instalar', 'morreu'),
(6, 1761, '2024-05-02 19:55:00', '2024-05-04 18:06:33', '2024-05-04 18:06:47', 'Atendido', 'Resolvido', 'SW', NULL, NULL, '2', '1', 'trocado'),
(7, 1761, '2024-05-02 19:59:00', '2024-05-04 18:12:48', '2024-05-04 18:13:07', 'Atendido', 'Resolvido', 'HW', 'rato', 'morreu', NULL, NULL, 's'),
(8, 1761, '2024-05-02 20:00:00', '2024-05-04 19:02:19', '2024-05-04 19:10:51', 'Atendido', 'Não resolvido', 'HW', 'rato', 'morreu', NULL, NULL, 'hyb'),
(9, 1761, '2024-05-02 20:01:00', NULL, NULL, 'Por atender', NULL, 'HW', 'Teclado', 'morreu', NULL, NULL, NULL),
(10, 1761, '2024-05-02 20:02:00', NULL, NULL, 'Por atender', NULL, 'HW', 'rato', 'morreu', '1', '2', NULL),
(11, 1761, '2024-05-02 21:34:52', '2024-05-02 21:35:27', '2024-05-04 18:00:05', 'Atendido', 'Resolvido', 'HW', 'rato', 'morreu', NULL, NULL, 'novo'),
(12, 1761, '2024-05-02 22:26:33', '2024-05-02 22:27:41', '2024-05-02 22:29:57', 'Atendido', 'Resolvido', 'HW', 'rato', 'morreu', NULL, NULL, 'Trocar fonte'),
(24, 0, '2024-05-04 18:27:44', NULL, NULL, 'Por atender', NULL, 'SW', NULL, NULL, 'windows', 'instalar', NULL),
(25, 1010, '2024-05-04 19:51:21', '2024-05-04 19:54:01', NULL, 'Em atendimento', 'Aberto', 'HW', 'RATO', 'morreu', NULL, NULL, NULL),
(26, 1010, '2024-05-04 19:52:13', '2024-05-04 19:52:27', NULL, 'Em atendimento', 'Aberto', 'SW', NULL, NULL, 'windoes', 'instalar', NULL);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`idTicket`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `ticket`
--
ALTER TABLE `ticket`
  MODIFY `idTicket` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
