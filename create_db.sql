-- Create the ITDB database
CREATE DATABASE ITDB;
GO

-- Use the ITDB database
USE ITDB;
GO

-- Create Attachments table
CREATE TABLE Attachments (
    id INT PRIMARY KEY,
    file_name NVARCHAR(50),
    file_size NVARCHAR(10),
    file_type NVARCHAR(10),
    date_of_upload DATETIME,
    uploader_id INT,
    task_id INT
);

-- Create UserNotifications table
CREATE TABLE UserNotifications (
    id INT PRIMARY KEY,
    notification_text NVARCHAR(50),
    creation_date DATETIME,
    addresser_id INT
);

-- Create TaskComments table
CREATE TABLE TaskComments (
    id INT PRIMARY KEY,
    comment NVARCHAR(200),
    date_of_creation DATETIME,
    user_id INT,
    task_id INT
);
