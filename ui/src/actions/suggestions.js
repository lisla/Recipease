const suggestionsLoaded = suggestions => ({
    type: 'Suggestions:LOADED',
    suggestions: suggestions
});

const getSuggestions = (query) => (dispatch, getState) => {
    let url = new URL('http://127.0.0.1:5000/associated');
    JSON.stringify(query);
    Object.keys(query).forEach(key => url.searchParams.append(key, query[key]));
    console.log(url);
    fetch(url.href, {
        method: 'GET'
    })
        .then(response => response.json())
        .then((suggestions) => dispatch(suggestionsLoaded(suggestions)))
        .catch(err => {
            console.error(err);
        });
};

export {
    getSuggestions
}
