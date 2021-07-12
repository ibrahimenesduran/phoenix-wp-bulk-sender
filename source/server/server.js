/*
Coded by Ibrahim Enes Duran
Started 01 July 2021 | Last Updated 01 July 2021

NOTICE! This program is coded for educational purposes.
If there is a data source violation, please contact the following communication channels.

ibrahimenesduran@hotmail.com
*/

const wppconnect = require('@wppconnect-team/wppconnect');
const moment = require('moment');  
const chalk = require('chalk')
const express = require('express')

const port = 8080
const app = express();

function Logger(type, msg){
    if(type == 1){
        console.log(`${moment().format('YYYY-MM-DD HH:mm:ss')} | ${chalk.red('ERROR')} | ${msg}`);
    }else{
        console.log(`${moment().format('YYYY-MM-DD HH:mm:ss')} | ${chalk.green('INFO ')} | ${msg}`);
    }

}


Logger(0, 'Server is starting...')
Logger(0, `Server is port: ${port}`)


wppconnect
  .create()
  .then((client) => start(client))
  .catch((error) => console.log(error));


function start(client) {
    app.use( express.json() );

    app.post( '/send', async (req, res) => {
        console.log(req.body)
        if(req.body.Number === undefined || req.body.Message === undefined){
            return res.sendStatus( 400 );
        }
        client
        .sendText(req.body.Number, req.body.Message)
        .then((result) => {
            res.status(200).end(JSON.stringify(result));
        }).catch((erro) => {
            res.status(400).end(JSON.stringify(erro)); 
        })

    } );
    
    app.listen(port, () => Logger(0, `Server started on port ${port}.` ) );
}
