import {useParams} from "react-router-dom";
import {useEffect, useState, useRef} from "react";
import {Grid} from "@mui/material";
import Slider from 'react-slick'
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

export default function GameDetails() {
    const {id} = useParams();
    const [game, setGame] = useState({});
    const mainSlider = useRef(null);
    const thumbSlider = useRef(null);

    const mainSettings = {
        asNavFor: thumbSlider.current,
        ref: mainSlider,
        slidesToShow: 1,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 3000,
        fade: true,
    };

    const thumbSettings = {
        asNavFor: mainSlider.current,
        ref: thumbSlider,
        slidesToShow: 5,
        swipeToSlide: true,
        focusOnSelect: true,
        arrows: false,
    };

    useEffect(() => {
        fetch(`http://api.trophyhunters.tech/games/${id}`)
            .then(res => res.json())
            .then(data => setGame(data))
    }, [id]);
    return (
        <Grid container className="lg:p-32 md:p-12 sm:p-5">
            <Grid size={{xs: 12, md: 12, lg: 5}} className="flex flex-col">
                <Slider {...mainSettings}>
                    {game.images?.map((image, index) => (
                        <div key={index}>
                            <img
                                src={image.url}
                                alt={`game image ${index + 1}`}
                                className="rounded-2xl"
                            />
                        </div>
                    ))}
                    {game.movies?.map((movie, index) => (
                        <div key={index}>
                            <video
                                src={movie.url}
                                muted controls
                                className="rounded-2xl"
                            />
                        </div>
                    ))}
                </Slider>

                <div className="mt-2">
                    <Slider {...thumbSettings}>
                        {game.images?.map((image, index) => (
                            <div key={index} className="px-2">
                                <img
                                    src={image.url}
                                    alt={`thumb ${index + 1}`}
                                    className="rounded cursor-pointer"
                                />
                            </div>
                        ))}
                        {game.movies?.map((movie, index) => (
                            <div key={index}>
                                <video
                                    src={movie.url}
                                    className="rounded cursor-pointer"
                                />
                            </div>
                        ))}
                    </Slider>
                </div>
            </Grid>

            <Grid size={{xs: 12, md: 12, lg: 7}}
                  className="flex flex-col gap-10 font-open justify-start text-white p-5 lg:max-h-[500px] overflow-y-auto scroll-hidden tracking-[2px]">
                <h1 className="text-[50px]">{game.name}</h1>
                <div className="flex flex-col gap-4 lg:text-[25px]">
                    <h2 className="pb-2 border-b-4 border-orange-400 w-fit">Description:</h2>
                    <p className="break-words">{game.description}</p>
                </div>
            </Grid>

            <Grid size={{xs: 12, md: 12, lg: 12}}
                  className="font-open text-white tracking-[2px] ">
                <h1 className="w-fit text-[40px] border-orange-500 border-b-4 pb-1 mb-5">Trophies:</h1>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 max-h-[400px] gap-5 overflow-y-auto scroll-hidden">
                    {game.trophies?.map((trophy,index) => (
                        <div key={index} className="flex gap-2 h-full object-contain">
                            <img src={trophy.blocked_icon} alt="trophy-icon" className="w-20 h-20 object-contain rounded-[15%]"/>
                            <div className="flex flex-col gap-2">
                                <span className="text-[20px] font-extrabold">{trophy.name}</span>
                                <p className="text-[13px]">{trophy.description}</p>
                            </div>
                        </div>
                    ))}
                </div>
            </Grid>
        </Grid>
    )
}