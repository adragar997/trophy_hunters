import {useEffect, useState} from "react";
import {Link} from "react-router-dom";
import Logo from '../assets/static/trophyhunters.png'
import {useUserContext} from "./Context/UserContext.jsx";
import DefaultAvatar from "../assets/static/defaultAvatar.png";

function NavComponent() {
    const [isOpen, setIsOpen] = useState(false);
    const {isLoggedIn, profile, logout} = useUserContext()

    return (
        <header className="w-full" style={{backgroundColor: '#D9D9D920'}}>
            <div className="flex items-center justify-between p-4">
                <Link to="/">
                    <img src={Logo} className="w-28"/>
                </Link>

                <button
                    className="lg:hidden text-white text-3xl"
                    onClick={() => setIsOpen(!isOpen)}
                >
                    {!isLoggedIn ? (
                        "☰"
                    ) : profile?.profile?.avatar ? (
                        <img
                            src={`http://api.trophyhunters.tech${profile.profile.avatar}`}
                            alt="avatar"
                            className="w-10 h-10 rounded-full"
                        />
                    ) : (
                        <img
                            src={DefaultAvatar}
                            alt="avatar"
                            className="w-10 h-10 rounded-full"
                        />
                    )}
                </button>

                <div className="hidden lg:flex gap-16 text-white text-xl font-open items-center tracking-widest">
                    <Link to="/">HOME</Link>
                    <Link to="/games">GAMES</Link>
                    <Link to="/news">NEWS</Link>
                    <Link to="/faq">FAQ</Link>
                </div>

                {!isLoggedIn && (
                    <div className="hidden lg:flex items-center gap-4">
                        <Link to="/login">
                            <button className="button">Login</button>
                        </Link>
                        <div className="w-[2px] h-8 bg-white"></div>
                        <Link to="/register">
                            <button className="button">Sign Up</button>
                        </Link>
                    </div>
                )}

                {isLoggedIn && (
                    <div className="relative hidden lg:flex items-center gap-2 text-white font-open tracking-[5px]">
                        <div onClick={() => setIsOpen(!isOpen)} className="flex items-center gap-2 cursor-pointer">
                            <img
                                src={profile?.profile?.avatar
                                    ? `http://api.trophyhunters.tech${profile.profile.avatar}`
                                    : DefaultAvatar}
                                className="w-[55px] h-[55px] rounded-[50%]"
                                alt="Avatar"
                            />
                            <span className="text-[15px] font-bold">{profile.username}</span>
                        </div>

                        {isOpen && (
                            <div
                                className="absolute top-full right-0 mt-2 w-40 bg-[#1a1a1a] rounded-xl shadow-lg z-50 p-3 flex flex-col gap-2 text-sm">
                                <Link to="/profile" onClick={() => setIsOpen(false)} className="hover:text-amber-500">
                                    Profile
                                </Link>
                                <Link to="/settings" onClick={() => setIsOpen(false)} className="hover:text-amber-500">
                                    Settings
                                </Link>
                                <button onClick={() => {
                                    logout();
                                    setIsOpen(false);
                                }} className="text-left hover:text-red-500">
                                    Logout
                                </button>
                            </div>
                        )}
                    </div>
                )}
            </div>

            {isOpen && (
                <div style={{backgroundColor: '#D9D9D920'}}
                     className="lg:hidden flex flex-col items-start gap-4 text-white px-6 pb-4 text-lg font-open">
                    <Link to="/" onClick={() => setIsOpen(false)}>HOME</Link>
                    <Link to="/games" onClick={() => setIsOpen(false)}>GAMES</Link>
                    <Link to="/news" onClick={() => setIsOpen(false)}>NEWS</Link>
                    <Link to="/faq" onClick={() => setIsOpen(false)}>FAQ</Link>
                    <div className="flex gap-3 pt-2">
                        <Link to="/login" onClick={() => setIsOpen(false)}>
                            <button className="button">Login</button>
                        </Link>
                        <Link to="/register" onClick={() => setIsOpen(false)}>
                            <button className="button">Logout</button>
                        </Link>
                    </div>
                </div>
            )}
        </header>
    )
}


export default NavComponent