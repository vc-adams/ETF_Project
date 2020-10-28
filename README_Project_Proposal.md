PROJECT PROPOSAL <br>
ETL PROJECT <br>
Group1 <br>
Team Members: Rob Pascarella, Vincent Adams, Emeka Obianyor  <br>
Project Summary: Pairing up insurance rates with weather data that can be searchable via user input. <br>
The idea of this project is to create a flask app to serve up to a client a bevy of data (in this case Auto insurance rates and weather data) for any zip code, city, or state that the client may requests. <br>
We have broken this project execution down into several phases: <br>

Extract: We need to extract all the data we intend to serve up to the client. In this case, Auto insurance rates – we intend to scrape insurance rates from various zip codes across the country. We will then pull weather data for same zip codes using API calls. <br>
Data sources: <br>
Auto Insurance data: <br>
https://www.autoinsurance.org/quoting-auto-insurance-rates-by-zip-code/ <br>
Weather data: <br>
http://api.openweathermap.org/api <br>

Transform: We will clean and merge the data from each resource. The creation and utiliztaion of a flask app will allow the user to extract auto insurance data as well as weather data for comparision and/or analysis. <br>

Load: We then intend to load said data into a postgres database, join the data tables by location, and prodcue the information via a search, all from our flask server. <br>

The flask app allows callalbe the data when a client requests information via each route. <br>
