const express = require('express')
const morgan = require('morgan')
const app = express()
const port = 8080

app.use(morgan('combined'))

app.get('/', (req, res) => {
    res.json({
        data: "Hello World!"
    })
})

app.listen(port, ()=>{
    console.log(`Apps runnig at port ${port}`)
})