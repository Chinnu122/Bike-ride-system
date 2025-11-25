// API helper functions
const API_BASE = '/api';

async function fetchAPI(endpoint, options) {
    const response = await fetch(`${API_BASE}${endpoint}`, options);
    return response.json();
}
