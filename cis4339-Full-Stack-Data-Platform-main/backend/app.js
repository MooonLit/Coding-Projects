// This is the main file for the backend

// import functionalities
const express = require("express");
const mongoose = require("mongoose");
const morgan = require("morgan");

const cors = require("cors");
const authMiddleware = require("./auth/authMiddleWare");
// allow using a .env file
require("dotenv").config(); //require the dotenv

// creates a new instance of express application
const app = express();

// add cors header to the server
app.use(
  cors({
    origin: "*",
  })
);

// suppress mongoose warning to prepare for new version
mongoose.set("strictQuery", false);

// sets up mongoose for the mongoDB connection
mongoose
  .connect(process.env.MONGO_URI)
  .then(() => {
    console.log("Database connection Success!");
  })
  .catch((err) => {
    console.error("Mongo Connection Error", err);
  });

// declare port number for the api
const PORT = process.env.PORT || 3000;

// setup and access request body
app.use(express.json());
app.use(morgan("dev"));
app.use(express.json());

// Request header logger for debugging
app.use((req, res, next) => {
  console.log("Incoming Request Headers:", req.headers);
  next();
});

// setup middle ware for routes
app.use("/clients", require("./routes/clients"));
app.use("/events", require("./routes/events"));
app.use("/orgs", require("./routes/org"));
app.use("/services", require("./routes/services")); // Temporarily remove authMiddleware for testing
app.use("/users", require("./routes/users"));

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});

// error handler
app.use(function (err, req, res, next) {
  console.error(err.stack); // Log the stack trace for detailed error info
  const statusCode = err.statusCode || 500;
  const message = statusCode >= 500 ? "Internal Server Error" : err.message;

  res.status(statusCode).send({ error: message });
});
