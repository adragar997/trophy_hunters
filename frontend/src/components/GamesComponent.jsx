import {useState, useEffect} from "react";
import {Grid} from '@mui/material'
import searchIcon from '../assets/static/searchIcon.png'
import {Link} from "react-router-dom";
import PaginationComponent from "./PaginationComponent.jsx";
import {motion} from "framer-motion";
import Free from '../assets/static/free.png'
import Paid from '../assets/static/paid.png'
import Trophy from '../assets/static/trophy.png'

function GamesComponent() {
    const [pagination, setPagination] = useState({next: null, previous: null});
    const [games, setGames] = useState([])
    const MotionGrid = motion.create(Grid);

    const fetchGames = async (url = 'http://127.0.0.1:8000/games/') => {
        const res = await fetch(url);
        const data = await res.json();
        setGames(data.results);
        setPagination({next: data.next, previous: data.previous});
    };

    const handleSearch = async (e) => {
        if (e.key === "Enter")
        await fetch(`http://127.0.0.1:8000/games/?name=${e.target.value}`)
            .then(res => res.json())
            .then(data => setGames(data.results))
    }

    useEffect(() => {
        fetchGames();
    }, []);

    return (
        <div>
            <div className="relative w-full max-w-md mx-auto mb-6">
                <input
                    type="text"
                    placeholder="Search"
                    className="w-full pr-12 rounded-3xl pl-5 font-open mt-10 p-2 tracking-widest focus:outline-none font-normal text-xl"
                    onKeyDown={handleSearch}
                />
                <img
                    src={searchIcon}
                    className="w-6 h-6 absolute right-4 top-3/4 transform -translate-y-1/2 cursor-pointer"
                    alt="Search"
                />
            </div>
            <Grid container spacing={6} className="p-10">
                {games.map(game => (
                    <MotionGrid
                        size={{sm: 12, md: 4, lg: 3}}
                        className="flex justify-center"
                        key={game.app_id}
                        initial={{y: 100, opacity: 0}}
                        animate={{y: 0, opacity: 1}}
                        transition={{duration: 1}}
                    >
                        <div className="relative">
                            <Link to={`/games/${game.app_id}`}>
                                <img src={game.cover} alt={game.name} className="rounded-3xl opacity-90"/>
                            </Link>
                            <img src={game.is_free ? Free : Paid} alt="free"
                                 className="absolute -bottom-2 -left-2 px-2 w-12 bg-gradient-to-r from-gray-400 to-black rounded-full "/>

                            <div
                                className="absolute flex gap-1 -top-5 -right-6 text-white bg-gradient-to-r from-yellow-600 to-orange-600 px-3 py-1 font-open text-[20px] tracking-widest rounded-full">
                                <img src={Trophy} alt="trophy" className="w-8"/>
                                <span>{game.trophy_count ? game.trophy_count : 0}</span>
                            </div>
                        </div>
                    </MotionGrid>
                ))}
            </Grid>
            <Grid size={{sm: 12, md: 12, lg: 12}} className=" pt-5 pb-5">
                <PaginationComponent
                    next={pagination.next}
                    previous={pagination.previous}
                    onPageChange={fetchGames}
                />
            </Grid>
        </div>
    )
}

export default GamesComponent