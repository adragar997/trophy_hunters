import {useState, useEffect} from "react";

function GamesComponent() {
    const [games, setGames] = useState([])

    useEffect(() => {
        const fetchData = async () => {
            const data = await fetch("http://127.0.0.1:8000/trophyhunters/games/")
            .then(res => res.json())
            console.log((data))
            setGames(data)
        }

        fetchData()
    }, [])

    return (
        <div>
            <h1>GAMES</h1>
            {games.map((game) => (
                <ul>
                    <li>{game.app_id}</li>
                    <li>{game.name}</li>
                    <li>{game.cover}</li>
                    <li>{game.trophy_count}</li>
                    <li>{game.price}</li>
                    <li>{game.age_requierd}</li>
                </ul>
            ))}
        </div>
    )
}

export default GamesComponent