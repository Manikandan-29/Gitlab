const express = require("express");
const app = express();

app.get("/", (req, res) => {
    res.send("<h2>Hi mani</h2>");
});

const port = process.env.PORT || 4000;
app.listen(port, () => console.log(`listening on port ${port}`));
