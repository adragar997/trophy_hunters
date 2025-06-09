import {Grid} from "@mui/material";
import {useEffect, useState} from "react";
import newTab from "../assets/static/newTab.png"
import PaginationComponent from "./PaginationComponent.jsx";
import {useUserContext} from "./Context/UserContext.jsx";

export default function NewsComponent() {
    const [gameNews, setNews] = useState([]);
    const [pagination, setPagination] = useState({next: null, previous: null});
    const {isLoggedIn, profile} = useUserContext()

    const fetchData = async (url = 'http://127.0.0.1:8000/news/') => {
        const res = await fetch(url);
        const data = await res.json();
        setNews(data.results);
        setPagination({next: data.next, previous: data.previous});
    };

    useEffect(() => {
        fetchData()
    }, []);

    return (
        <Grid container className="lg:p-48 p-10" spacing={4}>
            {gameNews.map(gameNew => (
                <Grid size={{xs: 12, md: 6, lg: 6}} className="flex flex-col lg:flex-row gap-4 text-white font-open">
                    <div className="min-w-[400px] h-[160px] lg:h-[150px]">
                        <img src={gameNew.cover} alt="gameCover" className="w-full h-full object-cover rounded-2xl"/>
                    </div>
                    <div className="flex flex-col gap-4 min-w-[250px]">
                        <span className="text-sm text-gray-300">{gameNew.date}</span>
                        <h1 className="text-xl font-bold">{gameNew.name}</h1>
                        <h2 className="text-base">{gameNew.title}</h2>
                        <a href={gameNew.url} target="_blank" className="w-fit">
                            <div className="rounded-2xl p-2 bg-teal-600 flex gap-2">
                                <span>
                                    Go to website
                                </span>
                                <img src={newTab} alt="tab" className="w-6 h-6"/>
                            </div>
                        </a>
                    </div>
                </Grid>
            ))}
            <Grid size={{sm: 12, md: 12, lg: 12}} className=" pt-5">
                <PaginationComponent
                    next={pagination.next}
                    previous={pagination.previous}
                    onPageChange={fetchData}
                />
            </Grid>
        </Grid>
    )
}