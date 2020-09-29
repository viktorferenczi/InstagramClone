import React, {useState, useEffect} from 'react';
import './App.css';
import axios from 'axios';

function App() {

    const [covidResults, setCovidResults] = useState({});


    useEffect(() => {
        axios.get('http://disease.sh/v3/covid-19/all?yesterday=false&twoDaysAgo=false&allowNull=true')
            .then( (response) => setCovidResults(response.data) );
        console.log(covidResults);
    }, [])

  return (
    <div className="App">
      woof
    </div>
  );
}

export default App;
