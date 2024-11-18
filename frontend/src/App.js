import React, { useState } from 'react';
import SearchBar from './SearchBar';
import SearchResults from './SearchResults';

function App() {
    const [results, setResults] = useState([]);

    const handleSearch = async (url, query) => {
        const response = await fetch(`/search?url=${url}&query=${query}`);
        const data = await response.json();
        setResults(data.results);
    };

    return (
        <div>
            <h1>Site Search Engine</h1>
            <SearchBar onSearch={handleSearch} />
            <SearchResults results={results} />
        </div>
    );
}

export default App;
