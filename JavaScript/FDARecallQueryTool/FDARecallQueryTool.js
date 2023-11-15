// Importing necessary modules
const express = require('express'); // Express framework for building web applications
const axios = require('axios'); // Axios for making HTTP requests
const app = express(); // Creating an instance of Express

// Setting up EJS as the view engine for rendering views
app.set('view engine', 'ejs');

// Middleware to parse URL-encoded data (from forms, for example)
app.use(express.urlencoded({ extended: true }));

// Serving static files (like CSS, JS, images) from the 'public' directory
app.use(express.static('public'));

// GET route for the root ('/') URL
// Renders the 'index' view when the root URL is accessed
app.get('/', (req, res) => {
  res.render('index');
});

// POST route for '/search'
// This route is invoked when the form on the index page is submitted
app.post('/search', async (req, res) => {
  // Reading the 'limit' field from the form data, defaulting to 5 if not provided
  const limit = req.body.limit || 5;
  
  // Constructing the API URL with the limit parameter
  const apiUrl = `https://api.fda.gov/food/enforcement.json?search=report_date:[20040101+TO+20131231]&limit=${limit}`;

  try {
    // Making an HTTP GET request to the API using Axios
    const response = await axios.get(apiUrl);
    // Extracting the 'results' array from the API response
    const recalls = response.data.results;
    // Rendering the 'results' view, passing the recalls data to it
    res.render('results', { recalls });
  } catch (error) {
    // Handling any errors that occur during the API request
    res.send('Error retrieving data');
  }
});

// Setting the port for the server to listen on
const PORT = process.env.PORT || 3000;

// Starting the server and listening on the specified port
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));