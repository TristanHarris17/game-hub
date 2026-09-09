import { useEffect, useState} from "react";
import { Link, useParams } from "react-router-dom";
import { getGame, getLatestPrice, getPriceHistory } from "../services/api";
import PriceHistoryChart from "../components/PriceHistoryChart";

function GameDetails() {
    const { gameId } = useParams();

    const [game, setGame] = useState(null);
    const [price, setPrice] = useState(null);
    const [priceHistory, setPriceHistory] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        async function loadGame() {
            try {
                const data = await getGame(gameId);
                setGame(data);

                const priceData = await getLatestPrice(gameId);
                setPrice(priceData);

                const priceHistoryData = await getPriceHistory(gameId);
                setPriceHistory(priceHistoryData);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        }

        loadGame();
    }, [gameId]);

    if (loading) {
        return <h1>Loading game details...</h1>
    }

    if (error) {
        return <h1>Error: {error}</h1>
    }
        
    return (
        <main className="game-details">
            <Link className="back-link" to="/">
                ← Back to Games
            </Link>

            <section className="game-header">
                <div className="game-header-image">
                    {game.thumbnail && (
                        <img src={game.thumbnail} alt={game.title} />
                    )}
                </div>

                <div className="game-header-info">
                    <h1>{game.title}</h1>

                    <div className="game-stats">
                        <p>
                            <strong>Steam Rating:</strong>{" "}
                            {game.steam_rating_percent ?? "N/A"}%
                        </p>

                        <p>
                            <strong>Reviews:</strong>{" "}
                            {game.steam_rating_count?.toLocaleString() ?? "N/A"}
                        </p>

                        <p>
                            <strong>On Sale:</strong>{" "}
                            {game.is_on_sale ? "Yes" : "No"}
                        </p>
                    </div>
                </div>
            </section>

            {price && (
                <section className="price-card">
                    <h2>Current Price</h2>

                    <div className="price-info">
                        <div>
                            <span>Normal Price</span>
                            <strong>${price.normal_price.toFixed(2)}</strong>
                        </div>

                        <div>
                            <span>Sale Price</span>
                            <strong>
                                {price.sale_price != null && game.is_on_sale
                                    ? `$${price.sale_price.toFixed(2)}`
                                    : "N/A"}
                            </strong>
                        </div>

                        <div>
                            <span>Savings</span>
                            <strong>
                                {price.savings != null && game.is_on_sale
                                    ? `${price.savings.toFixed(2)}%`
                                    : "N/A"}
                            </strong>
                        </div>
                    </div>
                </section>
            )}

            <section className="price-history-chart">
                <h2>Price History</h2>
                {priceHistory.length > 0 ? (
                    <PriceHistoryChart pricehistory={priceHistory} />
                ) : (
                    <p>No price history data is available.</p>
                )}
            </section>
        </main>
    );
}

export default GameDetails;