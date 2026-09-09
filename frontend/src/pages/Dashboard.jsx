import { useEffect, useState } from "react";
import { getGames } from "../services/api";
import GameTable from "../components/GameTable";

function Dashboard() {
    const [games, setGames] = useState([]);
    const [searchTerm, setSearchTerm] = useState("");
    const [showOnSaleOnly, setShowOnSaleOnly] = useState(false);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function loadGames() {
            try {
                const data = await getGames();
                setGames(data);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        }

        loadGames();
    }, []);

    const filteredGames = games.filter((game) => {
        const matchesSearch = game.title
            .toLowerCase()
            .includes(searchTerm.toLowerCase());
        
        const matchesSaleFilter = !showOnSaleOnly || game.is_on_sale;

        return matchesSearch && matchesSaleFilter;
    });

    if (loading) {
        return <h1>Loading games...</h1>
    }

    if (error) {
        return <h1>Error: {error}</h1>
    }

    return (
        <main className="dashboard">
            <header className="dashboard-header">
                <div>
                    <h1>Steam Deals</h1>
                    <p>Track game prices and discover deals.</p>
                </div>
            </header>

            <section className="dashboard-controls">
                <input
                    type="text"
                    placeholder="Search games..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                />

                <label>
                    <input
                        type="checkbox"
                        checked={showOnSaleOnly}
                        onChange={(e) => setShowOnSaleOnly(e.target.checked)}
                    />
                    {" "}Show games on sale only
                </label>
            </section>

            <section className="dashboard-summary">
                <p>
                    Showing <strong>{filteredGames.length}</strong> of{" "}
                    <strong>{games.length}</strong> games
                </p>
            </section>

            <GameTable games={filteredGames} />
        </main>
    );
}

export default Dashboard;