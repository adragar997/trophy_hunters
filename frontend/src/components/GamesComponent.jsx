import {useState, useEffect} from "react";

function GamesComponent() {
    const [games, setGames] = useState([])

    return (
        <div className="flex justify-center">
            <h1>games</h1>
        </div>
    )
}

export default GamesComponent