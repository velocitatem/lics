import express from 'express';
import bodyParser from 'body-parser';
import path from 'path'
const cors = require('cors')
const app = express();
var corsOptions = {
    origin: '*',
    optionsSuccessStatus: 200 // some legacy browsers (IE11, various SmartTVs) choke on 204
};

app.use(cors(corsOptions));
app.use(bodyParser.json()) // to process params

app.get("/stat", (req, res) => {
    res.status(200).send(`server is running`)
})


app.get("/make/:text", (req, res) => {

    const { exec } = require("child_process");
    exec(`python3 ~/lcs/lics-cli.py -m "${req.params.text}"`, (error,stdout,stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
        res.status(200).json([stdout]);
    });
    
})

//server log
app.listen(8050, () => console.log("server is listening on port 8000, happy coding"))
