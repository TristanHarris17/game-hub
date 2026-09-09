import {BrowserRouter, Routes, Route } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import GameDetails from './pages/GameDetails'

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route path="/game/:gameId" element={<GameDetails />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;