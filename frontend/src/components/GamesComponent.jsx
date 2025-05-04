import {useState, useEffect} from "react";

function GamesComponent() {
    const [games, setGames] = useState([])

    useEffect(() => {
        const fetchData = async () => {
            const data = await fetch("http://127.0.0.1:8000/trophyhunters/games/", {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('access')}`
                }
            })
            .then(res => res.json())
            setGames(data)
        }

        fetchData()
    }, [])

    return (
        <div>
            <h1>GAMES</h1>
            <ul>
                {games.map((game) => (
                    <li key={game.app_id}>{game.name}</li>
                ))}
            </ul>
        </div>
    )
}

export default GamesComponent