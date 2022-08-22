import express from 'express';
import bodyParser from 'body-parser';
import path from 'path'
const app = express();

app.use(express.static(path.join(__dirname, '/build'))) //to host a build website
app.use(bodyParser.json()) // to process params

app.get("/stat", (req, res) => {
    res.status(200).send(`server is running`)
})


app.get("/make/:text", (req, res) => {

    const { exec } = require("child_process");
    exec(`python3 /home/velo/Documents/Projects/LCS/lcs/lics-cli.py -m "${req.params.text}"`, (error,stdout,stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
        res.status(200).send(stdout)
    });
    
})

//server log
app.listen(80, () => console.log("server is listening on port 8000, happy coding"))
