import { Link } from "react-router-dom";

function GameTable({ games }) {
    
    return (
        <div className="game-table-container">
            <table className="game-table">
                <thead>
                    <tr>
                        <th>Game</th>
                        <th>Rating</th>
                        <th>Reviews</th>
                        <th>On Sale</th>
                    </tr>
                </thead>

                <tbody>
                    {games.map((game) => (
                        <tr key={game.id}>
                            <td>
                                {game.thumbnail && (
                                    <img
                                        className="game-table-thumbnail"
                                        src={game.thumbnail}
                                        alt={game.title}
                                    />
                                )}
                            </td>
                            <td>
                                <Link 
                                className="game-link"
                                to={`/game/${game.id}`}
                                >
                                {game.title}
                                </Link>
                            </td>

                            <td>
                                {game.steam_rating_percent
                                    ? `${game.steam_rating_percent}%`
                                    : "N/A"}
                            </td>

                            <td>
                                {game.steam_rating_count?.toLocaleString() ?? "N/A"}
                            </td>
                            
                            <td>
                                <span 
                                    className={
                                        game.is_on_sale
                                            ? "sale-badge"
                                            : "not-on-sale"
                                    }
                                >
                                    {game.is_on_sale ? "Yes" : "No"}
                                </span>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default GameTable;