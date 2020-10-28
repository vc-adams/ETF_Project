PROJECT PROPOSAL <br>
ETL PROJECT <br/>
Group1 <br/>
Team Members: Rob Pascarella, Vincent Adams, Emeka Obianyor  <br/>
Project Summary: Pairing up insurance rates with weather data that can be searchable via user input. <br/>
The idea of this project is to create a flask app to serve up to a client a bevy of data (in this case Auto insurance rates and weather data) for any zip code, city, or state that the client may requests. </br>
We have broken this project execution down into several phases. <br/>

Extract: We need to extract all the data we intend to serve up to the client. In this case, Auto insurance rates – we intend to scrape insurance rates from various zip codes across the country from here. We will then pull weather data for same zip codes using api calls from here. <br/>
Data sources: <br/>
Auto Insurance data: <br/>
https://www.autoinsurance.org/quoting-auto-insurance-rates-by-zip-code/ <br/>
Weather data: <br/>
http://api.openweathermap.org/api <br/>

Transform: We will clean the data from each source and then merge the data from each source and create a flask app that allows the user to extract auto insurance data as well as weather data for any state, city or zip code they chose. <br/>

Load: We intend to load said data into a postgres database and then join the data tables to get the information for our flask server. <br/>

We will then create a flask app to call the data when a client's requests information for a zip code or city. <br/>
