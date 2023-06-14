# <center>warehousing_app_command_line</center>

<div align="center">

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Paul-Mazu/warehousing_app?color=1d7147&style=for-the-badge) ![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/Paul-Mazu/warehousing_app?color=EAE6B4&style=for-the-badge) ![GitHub milestones](https://img.shields.io/github/milestones/all/Paul-Mazu/warehousing_app?color=F2F2F2&style=for-the-badge) ![GitHub language count](https://img.shields.io/github/languages/count/Paul-Mazu/warehousing_app?color=62B096&style=for-the-badge)
</div>

<div align="center">
  <a href="#about">About</a>  |
  <a href="#prerequisites">Prerequisites</a>  |
  <a href="#installation">Installation</a>  |
  <a href="#usage">Usage</a>  |
  <a href="#project-structure">Project Structure</a>  |
  <a href="#authors">Authors</a>
</div>

<br>

## About

The application is a showcase of backend (OOP) programming skills and knowledge of data types and pure structure of Python3.  

The Warehouse Management System is a command-line application that helps manage stock items in a warehouse.  
It provides functionality to search for items, place orders, and view available stock.  
The system also allows users to sign in as guests or registered users.  

## Prerequisites

- Python 3.x
- Required packages: `collections`

## Installation

1. Clone the repository: `git@github.com:Paul-Mazu/warehousing_app.git`  
2. Navigate to the project directory:`warehousing_app`  
3. Install the required packages:`pip install collections`  

## Usage

To start the application, run the following command:`python query.py`  


The application will prompt you with a menu of options:

1. List items by warehouse: Displays a list of all available items in the warehouse, grouped by warehouse and their quantities.  
2. Search an item and place an order: Allows you to search for a specific item by name and place an order if the item is available.  
3. Browse by category: Lists the available categories of items in the warehouse and allows you to search for items within a specific category.  
4. Quit: Exits the application and displays the search history.  

Follow the on-screen prompts to navigate through the application and perform the desired actions.  

## Project Structure

The project consists of the following files:

- `cli/data1.py`: Contains the initial stock data in a list format.
- `stock.py`: Defines functions for printing items, counting items by warehouse, searching items by name, and listing categories.
- `user.py`: Defines the `User` class responsible for user management and history tracking.
- `search.py`: Implements the item search functionality, including searching by name, searching by category, and checking for possible matches.
- `order.py`: Handles the item ordering process, including validating the order quantity and updating the user's order history.
- `query.py`: The main entry point of the application. It handles user authentication and presents the application menu.

Feel free to explore and modify the code according to your requirements.  



## Authors  

Pawel Mazurkiewicz:  
Tutor and Student Digital Career Institute  
[WWW](https://paul-mazu.github.io/portfolio/)  
[LinkedIn](https://www.linkedin.com/in/pawel-mazurkiewicz-906877173/) 
