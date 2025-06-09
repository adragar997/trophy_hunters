import {useState, useEffect} from "react";
import Slider from "react-slick";
import {Grid} from "@mui/material";
import TrophyIcon from '../assets/static/trophy.png'
import {motion} from "framer-motion";
import {Link} from "react-router-dom";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import newTab from "../assets/static/newTab.png";

export default function HomeComponent() {
    const [games, setGames] = useState([])
    const [news, setNews] = useState([])

    const fetchData = async () => {
        try {
            const gamesRes = await fetch('http://api.trophyhunters.tech/games/');
            const gamesData = await gamesRes.json();
            setGames(gamesData.results);
        } catch (error) {
            console.error("Error fetching games:", error);
            setGames([]);
        }

        try {
            const newsRes = await fetch('http://api.trophyhunters.tech/news/');
            const newsData = await newsRes.json();
            setNews(newsData.results);
        } catch (error) {
            console.error("Error fetching news:", error);
            setNews([]);
        }
    }

    useEffect(() => {
        fetchData();
    }, []);

    const settings = {
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        dots: false,
        autoplay: true,
        autoplaySpeed: 3000,
    };

    const minContentHeightClass = "min-h-[350px] sm:min-h-[400px] lg:min-h-[380px]";

    return (
        <Grid container justifyContent="center" spacing={3} className="text-white font-open p-5">
            {games.length > 0 && (
                <Grid size={{xs: 12, md: 12, lg: 6}} className="mt-5">
                    <h1 className="text-3xl sm:text-4xl lg:text-[40px] w-fit border-b-4 border-orange-400 mb-4 pb-1">New Games:</h1>
                    <Slider {...settings}>
                        {games.map(game => (
                            <div key={game.app_id} className={`overflow-y-auto scroll-hidden p-2 ${minContentHeightClass}`}>
                                <div className="flex flex-col lg:flex-row gap-4 h-full">
                                    <Grid size={{xs: 12, md: 12, lg: 6}} className="flex justify-center items-center">
                                        <Link to={`/games/${game.app_id}`} className="block w-full h-full">
                                            <img
                                                src={game.cover}
                                                alt={game.name}
                                                className="w-full h-auto object-cover rounded-lg shadow-md"
                                            />
                                        </Link>
                                    </Grid>
                                    <Grid size={{xs: 12, md: 12, lg: 6}}>
                                        <div className="flex flex-col gap-3 h-full">
                                            <div className="flex justify-between items-center text-sm text-gray-400">
                                                <span>{game.release_date}</span>
                                                <div className="flex gap-2 items-center">
                                                    <img src={TrophyIcon} alt="trophy icon" className="w-6 h-6"/>
                                                    <span>{game.trophy_count ? game.trophy_count : 0}</span>
                                                </div>
                                            </div>
                                            <h2 className="text-xl sm:text-2xl lg:text-[25px] font-extrabold line-clamp-2">{game.name}</h2>
                                            <div className="flex flex-wrap gap-2 text-xs overflow-y-auto scroll-hidden max-h-[80px]">
                                                {game.categories.map(category => (
                                                    <span
                                                        key={category.id}
                                                        className="bg-teal-600 px-2 py-1 text-black rounded-full whitespace-nowrap font-medium"
                                                    >
                                                        {category.name}
                                                    </span>
                                                ))}
                                            </div>
                                            <h2 className="text-lg sm:text-xl lg:text-[25px] border-b-4 border-orange-400 w-fit pb-1">Description:</h2>
                                            <p className="text-sm text-gray-300 leading-relaxed overflow-y-auto scroll-hidden flex-grow max-h-[120px]">
                                                {game.description}
                                            </p>
                                        </div>
                                    </Grid>
                                </div>
                            </div>
                        ))}
                    </Slider>
                </Grid>
            )}

            <Grid size={{xs: 12, md: 12, lg: 6}} className="mt-5">
                <h1 className="text-3xl sm:text-4xl lg:text-[40px] w-fit border-b-4 border-orange-400 mb-4 pb-1">News:</h1>
                <Slider {...settings}>
                    {news.map(gameNew => (
                        <div key={gameNew.id} className={`overflow-y-auto scroll-hidden p-2 ${minContentHeightClass}`}>
                            <div className="flex flex-col lg:flex-row gap-4 h-full">
                                <Grid size={{xs: 12, md: 12, lg: 6}} className="flex justify-center items-center">
                                    <img
                                        src={gameNew.cover}
                                        alt={gameNew.name}
                                        className="w-full h-auto object-cover rounded-lg shadow-md"
                                    />
                                </Grid>
                                <Grid size={{xs: 12, md: 12, lg: 6}}>
                                    <div className="flex flex-col gap-3 h-full">
                                        <span className="text-sm text-gray-400">{gameNew.date}</span>
                                        <h2 className="font-extrabold text-xl sm:text-2xl lg:text-[35px] line-clamp-2">{gameNew.name}</h2>
                                        <p className="text-sm text-gray-300 leading-relaxed line-clamp-3 lg:text-[20px] overflow-y-auto scroll-hidden flex-grow">
                                            {gameNew.title}
                                        </p>
                                        <a href={gameNew.url} target="_blank" rel="noopener noreferrer" className="w-fit mt-auto">
                                            <div className="rounded-full px-4 py-2 bg-teal-600 flex gap-2 items-center text-black font-semibold text-sm hover:bg-teal-500 transition-colors">
                                                <span>Go to website</span>
                                                <img src={newTab} alt="New Tab Icon" className="w-6 h-6"/>
                                            </div>
                                        </a>
                                    </div>
                                </Grid>
                            </div>
                        </div>
                    ))}
                </Slider>
            </Grid>

            <Grid size={{xs: 12, md: 12, lg: 6}} className="mt-5">
                <div className={`p-2 h-full flex items-center justify-center ${minContentHeightClass}`}>
                    <motion.div
                        className="flex h-full w-full justify-center items-center rounded-lg bg-gray-800/20"
                        key={2}
                        initial={{x: 100, opacity: 0}}
                        animate={{x: 0, opacity: 1}}
                        transition={{duration: 1}}
                    >
                        <h2 className="font-extrabold text-4xl sm:text-5xl lg:text-[50px] text-center text-gray-400">COMMING SOON</h2>
                    </motion.div>
                </div>
            </Grid>
        </Grid>
    )
}