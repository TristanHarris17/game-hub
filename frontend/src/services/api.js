const API_BASE_URL = "http://127.0.0.1:8000/api/v1"

export async function getGames() {
    const response = await fetch(
        `${API_BASE_URL}/games/`
    );

    if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`)
    }

    return response.json();
}

export async function getGame(gameId) {
    const response = await fetch(
        `${API_BASE_URL}/games/internal-id/${gameId}`
    );

    if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`)
    }

    return response.json();
}

export async function getLatestPrice(gameId) {
    const response = await fetch(
        `${API_BASE_URL}/pricing/${gameId}`
    );

    if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`)
    }

    return response.json();
}

export async function getPriceHistory(gameId) {
    const response = await fetch(
        `${API_BASE_URL}/pricing/${gameId}/history`
    );

    if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`)
    }

    return response.json();
}
