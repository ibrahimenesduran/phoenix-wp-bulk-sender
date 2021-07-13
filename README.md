<br />
<p align="center">
  <a href="https://github.com/ibrahimenesduran/phoenix-wp-bulk-sender">
    <img src="images/logo.png" alt="Logo" width="150">
  </a>

  <h3 align="center">Phoenix | Whatsapp Bulk Sender</h3>

  <p align="center">
  <br />
    <a href="https://github.com/ibrahimenesduran/phoenix-wp-bulk-sender">View Demo</a>
    ·
    <a href="https://github.com/ibrahimenesduran/phoenix-wp-bulk-sender/issues">Report Bug</a>
    ·
    <a href="https://github.com/ibrahimenesduran/phoenix-wp-bulk-sender/issues">Request Feature</a>
  </p>
</p>

<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about">About</a>
      <ul>
        <li><a href="#notice">Notice</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


## About

You will be able to send bulk messages on whatsapp web, with this program.

### Notice

This program is coded for educational purposes. If there is a data source violation, please contact the following communication channels.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Install requirement packages for server on Node.js
  ```sh
  cd ./source/server
  npm install express
  npm install moment
  npm install --save @wppconnect-team/wppconnect
  ```

* Install requirement packages for client on Python 3
  ```sh
  cd ./source/client
  pip install termcolor requests
  ```
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ibrahimenesduran/phoenix-wp-bulk-sender.git
   ```
1. Go inside source folder
   ```sh
   cd source
   ```
#### Server
1. Go inside server folder
   ```sh
   cd server
   ```
2. Run server.js
   ```sh
   node server.js
   ```
#### Client
1. Go inside client folder
   ```sh
   cd client
   ```
2. Run client.py
   ```sh
   python client.py
   ```

## License

Distributed under the MIT License. See LICENSE for more information.

## Contact

İbrahim Enes Duran - Istanbul Technical University - [LinkedIn](https://linkedin.com/in/ibrahimenesduran)
