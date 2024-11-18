import React, { useState } from 'react';

function SearchBar({ onSearch }) {
    const [url, setUrl] = useState('');
    const [query, setQuery] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSearch(url, query);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Enter website URL"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
            />
            <input
                type="text"
                placeholder="Enter search query"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />
            <button type="submit">Search</button>
        </form>
    );
}

export default SearchBar;
